# Generated by Django 3.1.7 on 2021-03-21 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_renameFields'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='is_tutor',
            field=models.CharField(choices=[('Regular User', 'Regular User'), ('Tutor', 'Tutor')], default=None, max_length=15, verbose_name='Type of Account: (Tutor/Regular)'),
        ),
    ]
