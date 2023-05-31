from django.db import models

#Статьи
class Article(models.Model):

    title = models.CharField("Название", max_length=100)
    text = models.TextField("Текст")
    department = models.ForeignKey("knowledge_base_app.department", on_delete=models.CASCADE, related_name="articles", 
                                   verbose_name="Отдел")
    category = models.ForeignKey("knowledge_base_app.category", on_delete=models.CASCADE, related_name="articles", 
                                 verbose_name="Категория")
    language = models.ForeignKey("knowledge_base_app.language", on_delete=models.CASCADE, related_name="articles", 
                                 verbose_name="Язык")
    tags = models.ManyToManyField("knowledge_base_app.tag", related_name="articles", verbose_name="Теги")
    cre_user = models.ForeignKey("knowledge_base_app.user", on_delete=models.CASCADE, related_name="articles", 
                                 verbose_name="Создатель")
    create_time = models.DateTimeField("Дата создания", auto_now_add=True)
    update_time = models.DateTimeField("Дата обновлени", auto_now=True)

    class Meta:
        ordering = ["title"]
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"

    def __str__(self) -> str:
        return self.title

