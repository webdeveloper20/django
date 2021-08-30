import article
from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.


class Article(models.Model):
    author = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE, verbose_name="Yazar")
    title = models.CharField(max_length=50, verbose_name="Baslik")
    content = RichTextField()
    created_data = models.DateTimeField(
        auto_now_add=True, verbose_name="Olusturma tarixi")
    article_image = models.FileField(
        blank=True, null=True, verbose_name="Mekaleye fotograf ekleyin")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created_data']


class Comment(models.Model):
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, verbose_name="Makele", related_name="comments")
    comment_author = models.CharField(max_length=50, verbose_name="Isim")
    comment_content = models.CharField(max_length=200, verbose_name="Comment")
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_content

    class Meta:
        ordering = ['comment_date']
