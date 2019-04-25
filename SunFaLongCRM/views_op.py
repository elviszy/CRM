from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from rest_framework.mixins import CreateModelMixin,RetrieveModelMixin,UpdateModelMixin
from rest_framework.response import Response
from rest_framework import viewsets,status
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework import authentication
from rest_framework_jwt.serializers import jwt_decode_handler,jwt_payload_handler

from .myserializers import AddUserSerializers,UserDetailSerializers,UpdatePWDSerializers

# Create your views here.

User = get_user_model()
class CustomBackend(ModelBackend):
    """
    自定义用户认证
    """
    def authenticate(self,username=None,password=None,**kwargs):
        try:
            user = User.objects.get(Q(username=username)|Q(mobile=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class UpdatePWDView(RetrieveModelMixin,UpdateModelMixin,viewsets.GenericViewSet):
    serializer_class = UpdatePWDSerializers
    queryset = User.objects.all()


    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        ret = {}
        serializer.is_valid(raise_exception=True)
        username = request.data['username']
        user = User.objects.get(username=username)
        user.set_password(request.data['password'])
        user.save()
        ret['username'] = user.username
        ret['msg'] = "修改成功"
        return Response(ret,status=status.HTTP_201_CREATED)
    def get_object(self):
        return self.request.user







class AddUserView(CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,viewsets.GenericViewSet):
    serializer_class = AddUserSerializers
    queryset = User.objects.all()
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)



    def get_serializer_class(self):
        if self.action == "retrieve":
            return UserDetailSerializers
        elif self.action == "create":
            return AddUserSerializers

        return UserDetailSerializers

    def get_object(self):
        return self.request.user

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     user = self.perform_create(serializer)
    #
    #     re_dict = serializer.data
    #     payload = jwt_payload_handler(user)
    #     re_dict["token"] = jwt_decode_handler(payload)
    #     re_dict["name"] = user.name if user.name else user.username
    #
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)
    #
    # def perform_create(self, serializer):
    #     return serializer.save()

