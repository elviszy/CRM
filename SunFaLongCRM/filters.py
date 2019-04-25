import django_filters as filter
from .models import CustomerInfo

class CustFilters(filter.rest_framework.FilterSet):
    """
    自定义客户信息过滤
    """
    name = filter.CharFilter(field_name='name',lookup_expr='icontains')
    class Meta:
        model = CustomerInfo
        fields = ['name', 'cert_num','contact']
