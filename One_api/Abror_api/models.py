from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100,null=False,blank=False)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=250,null=False,blank=False)
    body = models.TextField(blank=False,null=False)
    author = models.ForeignKey(Author,null=True,blank=True,on_delete=models.SET_NULL)

    def __str__(self):
        return self.title