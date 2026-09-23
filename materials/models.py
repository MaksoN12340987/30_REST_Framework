from django.db import models

class Lesson(models.Model):
    title = models.CharField(verbose_name="Название урока")
    description = models.CharField(blank=True, default="Опиcание скоро появится", verbose_name="Описание урока")
    preview = models.ImageField(upload_to="lesson/", verbose_name="Фотография", null=True, blank=True)
    video_link = models.CharField(verbose_name="Сылка на видео")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
        ordering = ["id", "title"]


class Course(models.Model):
    title = models.CharField(verbose_name="Название курса")
    preview = models.ImageField(upload_to="couse/", verbose_name="Фотография", null=True, blank=True)
    description = models.CharField(blank=True, default="Без опиcания", verbose_name="Описание курса")
    lessons = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name="Уроки курса")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"
        ordering = ["id", "title"]
