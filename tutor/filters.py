import django_filters
from .models import TutorProfile, Subject


class TutorFilter(django_filters.FilterSet):
    model = TutorProfile

    fee = django_filters.NumberFilter(field_name='fee', lookup_expr='lte', label='Price Cap ($/hr):')
    rating = django_filters.NumberFilter(field_name='rating', lookup_expr='gte', label='Minimum Tutor Rating:')
    # ^figure out how to make a selection by clicking one of 5 stars.

    METHOD_CHOICES = (  # used exclude in order to remove 'both'
        ('In-Person', 'Online'),
        ('Online', 'In-Person')
    )

    subjects = Subject.objects.all()
    SUBJECT_CHOICES = []
    for subject in subjects:
        name = subject.name
        SUBJECT_CHOICES.append((name, name))

    method = django_filters.ChoiceFilter(field_name='method', label='Select Method:',
                                         empty_label='Choose... ', choices=METHOD_CHOICES, exclude=True)
    subjects_filter = django_filters.ChoiceFilter(field_name='subjects', label='Select Subject:',
                                                  empty_label='Choose... ', choices=SUBJECT_CHOICES)
