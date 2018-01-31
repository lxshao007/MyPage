from django.db import models

class Vistor(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    message = models.TextField(max_length=264)

    def __str__(self):
        return self.name
