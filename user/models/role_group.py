from django.db import models

#Группы ролей
class Role_group(models.Model):
    name = models.CharField("Название", max_length=100)
    roles = models.ManyToManyField("knowledge_base_app.user_role", related_name="role_groups", verbose_name="Роли")
    create_time = models.DateTimeField("Дата создания", auto_now_add=True)
    update_time = models.DateTimeField("Дата обновлени", auto_now=True)

    class Meta:
        verbose_name = "Группа роли"
        verbose_name_plural = "Группы ролей"

    def __str__(self) -> str:
        return self.name
