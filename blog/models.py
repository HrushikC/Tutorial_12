from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class TutorProfile(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    # subjects = models.---Choices()---
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('profile-detail', kwargs={'pk': self.pk})
