# Generated by Django 4.2.4 on 2023-10-15 10:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organisation', '0006_remove_invitation_expiry_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invitation',
            name='organisation',
        ),
        migrations.RemoveField(
            model_name='invitation',
            name='user',
        ),
    ]
