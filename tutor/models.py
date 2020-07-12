from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class TutorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    # subjects = models.CharField(max_length=300)
    zipcode = models.CharField(max_length=5, default=None)
    tutor_methods = models.TextChoices('medium of instruction', 'Online In-Person Both')
    method = models.CharField(choices=tutor_methods.choices, max_length=10, default=None)
    resume = models.FileField(default=None, upload_to='resumes')
    rating = models.FloatField(default=None)
    fee = models.IntegerField(default=None)
    travel_distance = models.IntegerField(default=0)
    is_hidden = models.BooleanField(default=False)
    date_posted = models.DateTimeField(default=timezone.now)

    # author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.account.name

    def get_absolute_url(self):
        return reverse('profile-detail', kwargs={'username': self.account.user})
