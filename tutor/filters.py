import django_filters
from .models import TutorProfile


class TutorFilter(django_filters.FilterSet):
    model = TutorProfile

    fee = django_filters.NumberFilter(field_name='fee', lookup_expr='lt', label='Price Cap ($/hr):')
    rating = django_filters.NumberFilter(field_name='rating', lookup_expr='gt', label='Minimum Tutor Rating:')

    METHOD_CHOICES = (
        ('In-Person', 'Online'),
        ('Online', 'In-Person')
    )
    method = django_filters.ChoiceFilter(field_name='method', label='Select Method:',
                                         empty_label='Choose...', choices=METHOD_CHOICES, exclude=True)

