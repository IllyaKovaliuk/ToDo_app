from django.db import models


# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=50)


class Task(models.Model):
    content = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()
    done_not_done = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag)

