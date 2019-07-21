from django_filters import filters
from django_filters import FilterSet
from .models import Job


class MyOrderingFilter(filters.OrderingFilter):
    descending_fmt = '%s （降順）'


class JobFilter(FilterSet):

    name = filters.CharFilter(label='名前', lookup_expr='contains')
    memo = filters.CharFilter(label='備考', lookup_expr='contains')

    order_by = MyOrderingFilter(
        # tuple-mapping retains order
        fields=(
            ('name', 'name'),
            # ('age', 'age'),
        ),
        field_labels={
            'name': '名前',
            # 'age': '年齢',
        },
        label='並び順'
    )

    class Meta:

        model = Job
        fields = ('name', 'memo', 'send_date')