from django.db import models
from django.contrib.auth.models import AbstractUser

#Пользователи
class User(AbstractUser):
    department = models.ForeignKey("department.department", on_delete=models.CASCADE, related_name="users", 
                                   verbose_name="Отдел")
    role_group = models.ForeignKey("user.role_group", on_delete=models.CASCADE, related_name="users", 
                                   verbose_name="Группа ролей")

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self) -> str:
        return self.username

