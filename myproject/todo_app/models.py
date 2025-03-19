from django.db import models


# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=50)


class Task(models.Model):
    name = models.CharField(max_length=50, default='')
    content = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()
    done_not_done = models.BooleanField(default=False)
    tags = models.ManyToManyField('Tag', blank=True)  # важливо: blank=True

    def __str__(self):
        return self.tags
