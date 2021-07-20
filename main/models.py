from django.db import models
# Create your models here.

class TrainingList(models.Model):
    title = models.CharField(max_length = 200, primary_key=True)
    kind = models.CharField(max_length= 200)
    body = models.TextField()

    def __str__(self):
        return self.title

class TrainingImage(models.Model):
    title = models.ForeignKey(TrainingList, default=None, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images')

class UserInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    nickname = models.CharField(max_length=20)