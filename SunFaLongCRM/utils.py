import hashlib

from rest_framework.pagination import PageNumberPagination
from rest_framework import exceptions


from rest_framework.authentication import BaseAuthentication


from .models import *
class TokenAuth(BaseAuthentication):
    def authenticate(self,request):
        token = request.GET.get("token")
        token_obj = UserToken.objects.filter(token=token).first()
        if not token_obj:
            raise exceptions.AuthenticationFailed("登录验证失败，请重新登录!")
        else:
            return token_obj.user.name,token_obj.token


class CustInfoPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 100




def md5(arg):
    hash = hashlib.md5()
    hash.update(bytes(arg,encoding='utf-8'))
    return hash.hexdigest()

