from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=50, default='')
    content = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()
    done_not_done = models.BooleanField(default=False)
    tags = models.ManyToManyField('Tag', blank=True)

    def __str__(self):
        return self.tags
