from django.db import models

# Create your models here.
class Tag(models.Model):
    tagName=models.CharField(max_length=200)

    def __str__(self):
        return f"{self.tagName}"

class Author(models.Model):
    first_name=models.CharField(max_length=40)
    last_name=models.CharField(max_length=20)
    email=models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Post(models.Model):
    title=models.CharField(max_length=200)
    image=models.CharField(max_length=200)
    author=models.ForeignKey(Author,on_delete=models.SET_NULL,null=True)
    slug=models.SlugField(unique=True)
    excerpt=models.CharField(max_length=500  )
    content=models.CharField(max_length=500)
    data=models.DateField(auto_now=True)
    tag=models.ManyToManyField(Tag)



