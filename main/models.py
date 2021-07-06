from django.db import models
from django.db.models.fields.related import ManyToManyField
# Create your models here.


class TrainingList(models.Model):
    title = models.CharField(max_length = 200)
    kind = models.CharField(max_length= 200)
    body = models.TextField()

    def __str__(self):
        return self.title

class TrainingImages(models.Model):
    post = models.ForeignKey(TrainingList, default=None, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images')