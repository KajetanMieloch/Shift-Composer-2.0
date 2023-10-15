from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    surename = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='profile_pics', blank=True)
    # other fields...

    def __str__(self):
        return self.user.username