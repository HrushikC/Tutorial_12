# Generated by Django 3.1.7 on 2021-04-01 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutor', '0009_switched_m2m_loc'),
        ('users', '0004_account_created_tutorprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='tutorprofiles',
            field=models.ManyToManyField(default=None, to='tutor.TutorProfile', verbose_name='My Tutors'),
        ),
    ]
