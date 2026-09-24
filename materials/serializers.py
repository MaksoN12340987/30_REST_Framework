import logging
from rest_framework import serializers
from django.core.cache import cache

from .models import Course, Lesson

logger_serializers_materials = logging.getLogger(__name__)
file_handler = logging.FileHandler(f"log/{__name__}.log", mode="a", encoding="UTF8")
file_formatter = logging.Formatter(
    "\n%(asctime)s %(levelname)s %(name)s \n%(funcName)s %(lineno)d: \n%(message)s",
    datefmt="%H:%M:%S %d-%m-%Y",
)
file_handler.setFormatter(file_formatter)
logger_serializers_materials.addHandler(file_handler)
logger_serializers_materials.setLevel(logging.INFO)


class CourseSerializer(serializers.ModelSerializer):
    lessons = cache.get("CourseSerializer_queryset")
    if not lessons:
        lessons = serializers.SerializerMethodField()
        cache.set("CourseSerializer_queryset", lessons, 60 * 15)
    
    def get_lessons(self, instance):
        qeryset_lessons = instance.lesson_set.all()
        logger_serializers_materials.info(qeryset_lessons)
        
        lessons_str = ', '.join(obj.title for obj in qeryset_lessons)
        return lessons_str

    class Meta:
        model = Course
        fields = "__all__"


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"
