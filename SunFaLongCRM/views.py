from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import authentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView

import json

from SunFaLongCRM.utils import CustInfoPagination,md5
from .models import *
from .filters import CustFilters
from SunFaLongCRM import myserializers,forms


class CustInfoModelView(viewsets.ModelViewSet):
    queryset = CustomerInfo.objects.all().order_by('-create_date')
    serializer_class = myserializers.CustinfoModelSerializers
    pagination_class = CustInfoPagination
    filter_backends = (DjangoFilterBackend,)
    filter_class = CustFilters
    permission_classes = []

    # authentication_classes = (JSONWebTokenAuthentication,authentication.SessionAuthentication)


    #分页展示
    # def list(self, request, *args, **kwargs):
    #     cust = CustomerInfo.objects.all().order_by('-create_date')
    #     pp = CustInfoPagination()
    #     pager_custs = pp.paginate_queryset(cust,request,self)
    #     cust_list = myserializers.CustinfoModelSerializers(pager_custs,many=True)
    #     return pp.get_paginated_response(cust_list.data)
        # return Response(cust_list.data)









