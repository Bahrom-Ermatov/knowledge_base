from django.db import models

#Язык
class Language(models.Model):
    name = models.CharField("Название", max_length=100)
    create_time = models.DateTimeField("Дата создания", auto_now_add=True)
    update_time = models.DateTimeField("Дата обновлени", auto_now=True)

    class Meta:
        verbose_name = "Язык"
        verbose_name_plural = "Языки"

    def __str__(self) -> str:
        return self.name

