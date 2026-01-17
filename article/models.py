from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Article(models.Model):
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name="Yazar" )
    title = models.CharField(max_length= 150,verbose_name="Baslik")
    content = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Olusturulma Tarihi") 
    article_image = models.FileField(blank = True, null= True,verbose_name="MAKALE RESMINI EKLEYIN")
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_date']
class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete = models.CASCADE,verbose_name = "Makale",related_name="comments")
    comment_author = models.CharField(max_length = 50,verbose_name = "İsim")
    comment_content = models.CharField(max_length = 400,verbose_name = "Yorum")
    comment_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment_author
    class Meta:
        ordering = ['-comment_date']