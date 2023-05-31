from django.db import models

#Комментарий
class Comment(models.Model):

    text = models.CharField("Текст", max_length=2000)
    article = models.ForeignKey("knowledge_base_app.article", on_delete=models.CASCADE, related_name="comments", 
                                verbose_name="Отдел")
    cre_user = models.ForeignKey("knowledge_base_app.user", on_delete=models.CASCADE, related_name="comments", 
                               verbose_name="Создатель", null=True)
    create_time = models.DateTimeField("Дата создания", auto_now_add=True)
    update_time = models.DateTimeField("Дата обновлени", auto_now=True)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self) -> str:
        return self.text

