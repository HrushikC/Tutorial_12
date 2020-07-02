from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class TutorProfile(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    # subjects = models.---Choices()---
    # online = true;false
    # rating = unrated; double
    # fee = option of fee; free
    # location = get location from ip address; field to get number of miles they are willing to travel.
    # profile_status = hidden;shown
    date_posted = models.DateTimeField(default=timezone.now)

    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    # will replace author with user^ after new database where each account has only one tutorprofile

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('profile-detail', kwargs={'pk': self.pk})
