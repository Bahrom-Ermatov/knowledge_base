from django.db import models

#Отдел
class Department(models.Model):
    name = models.CharField("Название", max_length=100)
    create_time = models.DateTimeField("Дата создания", auto_now_add=True)
    update_time = models.DateTimeField("Дата обновлени", auto_now=True)

    class Meta:
        verbose_name = "Отдел"
        verbose_name_plural = "Отделы"

    def __str__(self) -> str:
        return self.name

