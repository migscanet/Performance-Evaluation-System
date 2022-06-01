import django_filters
from .models import *

class DeptUnitFilter(django.FilterSet)
    DEPT_CHOICES =(
        ('mcsu', 'Mathematical and Computational Sciences Unit'),
        ('chem', 'Chemistry Unit'),
        ('pgu', 'Physics and Geology Unit')
    )

    class Meta:
        model = User

    order_