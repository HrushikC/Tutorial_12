import django_filters
from .models import TutorProfile, Subject


class TutorFilter(django_filters.FilterSet):
    model = TutorProfile

    fee = django_filters.NumberFilter(field_name='fee', lookup_expr='lte', label='Price Cap ($/hr):')
    rating = django_filters.NumberFilter(field_name='rating', lookup_expr='gte', label='Minimum Tutor Rating:')

    METHOD_CHOICES = (
        ('In-Person', 'Online'),
        ('Online', 'In-Person')
    )
    method = django_filters.ChoiceFilter(field_name='method', label='Select Method:',
                                         empty_label='Choose...', choices=METHOD_CHOICES, exclude=True)
    # subjects = django_filters.ChoiceFilter(field_name='subjects', label='Select Subject(s):',
    #                                        empty_label='Choose', choices=Subject.objects.all())
