from django.db import models

#Роли пользователей
class User_role(models.Model):
    name = models.CharField("Название", max_length=100)
    create_time = models.DateTimeField("Дата создания", auto_now_add=True)
    update_time = models.DateTimeField("Дата обновлени", auto_now=True)

    class Meta:
        verbose_name = "Роль"
        verbose_name_plural = "Роли"

    def __str__(self) -> str:
        return self.name


