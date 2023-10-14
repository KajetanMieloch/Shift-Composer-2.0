# Generated by Django 4.2.5 on 2023-10-13 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('members', models.ManyToManyField(related_name='user_profiles', to='core.userprofile')),
            ],
        ),
    ]
