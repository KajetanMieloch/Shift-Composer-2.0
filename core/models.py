from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    in_organisation = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    # other fields...

    def __str__(self):
        return self.user.username