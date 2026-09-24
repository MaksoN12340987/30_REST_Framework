from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .apps import MaterialsConfig
from .views import CourseViewSet, CreateLessonAPI, DeleteLessonAPI, LessonAPI, LessonsAPI, UpdateLessonAPI

app_name = MaterialsConfig.name

router = DefaultRouter()
router.register(r'cource', CourseViewSet, basename='cource')

urlpatterns = [
    path("", include(router.urls)),
    path("lessons/", LessonsAPI.as_view(), name="lessons"),
    path("lesson/<int:pk>/", LessonAPI.as_view(), name="lesson"),
    path("lesson/<int:pk>/update/", UpdateLessonAPI.as_view(), name="update"),
    path("lesson/<int:pk>/delete/", DeleteLessonAPI.as_view(), name="delete"),
    path("lesson/", CreateLessonAPI.as_view(), name="create"),
]
