import django_filters
from .models import TutorProfile


class TutorFilter(django_filters.FilterSet):

    class Meta:
        model = TutorProfile
        fields = {
            'fee': ['lt', 'gt'],
            'rating': ['gt'],
            'method': []
        }