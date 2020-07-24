from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class TutorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    subject_details = models.TextField(default="")
    zipcode = models.CharField(max_length=5, default=None)
    tutor_methods = models.TextChoices('medium of instruction', 'Online In-Person Both')
    method = models.CharField(choices=tutor_methods.choices, max_length=10, default=None)
    resume = models.FileField(default=None, upload_to='resumes', blank=True)
    rating = models.FloatField(default=0)
    review_count = models.IntegerField(default=0)
    fee = models.IntegerField(default=None)
    contact_info = models.TextField(default="Text or Call 555-555-5555")
    travel_distance = models.IntegerField(default=0)
    is_hidden = models.BooleanField(default=False)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('profile-detail', kwargs={'pk': self.user.id})


class Subject(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(default=None)
    tutor_profile = models.ManyToManyField(TutorProfile)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
