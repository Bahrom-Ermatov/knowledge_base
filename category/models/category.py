from django.db import models

#Категория
class Category(models.Model):
    name = models.CharField("Название", max_length=100)
    create_time = models.DateTimeField("Дата создания", auto_now_add=True)
    update_time = models.DateTimeField("Дата обновлени", auto_now=True)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, 
                               blank=True, null=True,
                               related_name="subcategories", 
                               verbose_name="Родительская категория")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self) -> str:
        return self.name
