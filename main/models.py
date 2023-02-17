from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=255)



class Test(models.Model):
    text = models.TextField()
    true = models.CharField(max_length=255)
    false = models.CharField(max_length=255)
    false_2 = models.CharField(max_length=255)
    false_3 = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)


class Advertisement(models.Model):
    url = models.URLField()
    name = models.CharField(max_length=255)
    video = models.FileField(upload_to="Advertisement/")


class Chat(models.Model):
    message = models.TextField()
    names = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
