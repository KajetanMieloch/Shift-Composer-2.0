from django.db import models

class Organisation(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    admins = models.ManyToManyField('core.UserProfile', related_name='admins')
    members = models.ManyToManyField('core.UserProfile', related_name='user_profiles')


    def __str__(self):
        return self.name

class Invitation(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=9)
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE)
    expires = models.DateTimeField()

    def __str__(self):
        return self.code