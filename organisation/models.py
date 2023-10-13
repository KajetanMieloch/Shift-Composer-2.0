from django.db import models

class Organisation(models.Model):
    name = models.CharField(max_length=100)
    admins = models.ManyToManyField('core.UserProfile', related_name='admins')
    members = models.ManyToManyField('core.UserProfile', related_name='user_profiles')


    def __str__(self):
        return self.name