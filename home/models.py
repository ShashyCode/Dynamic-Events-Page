from django.db import models

# Create your models here.
class Events(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField()
    time = models.TimeField(auto_now=False, auto_now_add=False)
    location = models.CharField(max_length=50)
    liked = models.BooleanField(default=False)

    img = models.ImageField(upload_to='media/', height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return self.name


