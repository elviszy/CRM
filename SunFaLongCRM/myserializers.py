from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator

from .models import CustomerInfo,Records

User = get_user_model()

class RecordsModelSerializers(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    class Meta:
        model = Records
        fields = ("content","user")
        # depth =2

    def get_user(self, obj):
        return obj.user.name if  obj.user.name else obj.user.username



class CustinfoModelSerializers(serializers.ModelSerializer):
    content = RecordsModelSerializers(many=True,required=False,allow_null=True)
    class Meta:
        model = CustomerInfo
        fields = "__all__"


class AddUserSerializers(serializers.ModelSerializer):
    username = serializers.CharField(required=True, allow_blank=False, min_length=5,
                                     validators=[UniqueValidator(queryset=User.objects.all(), message="用户已存在")],
                                     error_messages={
                                         "blank": "请输入用户名！",
                                         "required": "请输入用户名！",
                                         "max_length": "用户名不能小于5位"
                                     })
    password = serializers.CharField(
        style={'input_type': 'password'}, min_length=6, write_only=True, required=True, error_messages={
            "blank": "请输入密码！",
            "required": "请输入密码！",
            "min_length": "密码不能少于6位"
        }
    )
    re_password = serializers.CharField(required=True, write_only=True,
                                        style={'input_type': 'password'}, error_messages={
            "blank": "请输入确认密码！",
            "required": "请输入确认密码！"
        }
     )

    # def create(self, validated_data):
    #     user = super(AddUserSerializers,self).create(validated_data=validated_data)
    #     user.set_password(validated_data["password"])
    #     user.save()
    #     return user

    def validate_re_password(self, re_password):
        if re_password != self.initial_data['password']:
            raise serializers.ValidationError("两次输入密码不一致")

    def validate(self, attrs):
        attrs["mobile"] = attrs["username"]
        del attrs["re_password"]
        return attrs

    class Meta:
        model = User
        fields = ("username", "password", "re_password", "mobile")


class UserDetailSerializers(serializers.ModelSerializer):
    """
    用户详情序列化
    """
    username = serializers.CharField(read_only=True)
    class Meta:
        model = User
        fields = ("username", "name", "mobile")

class UpdatePWDSerializers(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'}, min_length=6, write_only=True, required=True, error_messages={
            "blank": "请输入旧密码！",
            "required": "请输入旧密码！",
            "min_length": "密码不能少于6位"
        }
    )
    new_password = serializers.CharField(
        style={'input_type': 'password'}, min_length=6, write_only=True, required=True, error_messages={
            "blank": "请输入新密码！",
            "required": "请输入新密码！",
            "min_length": "密码不能少于6位"
        }
    )
    re_new_password = serializers.CharField(required=True, write_only=True,
                                        style={'input_type': 'password'}, error_messages={
            "blank": "请输入确认密码！",
            "required": "请输入确认密码！"
        }
     )

    def validate_password(self,password):
        user = User.objects.get(username=self.initial_data['username'])
        if not user.check_password(password):
            raise serializers.ValidationError("旧密码不正确")
    def validate_new_password(self,new_password):
        if new_password == self.initial_data['password']:
            raise serializers.ValidationError("新密码不能与旧密码相同！")


    def validate_re_new_password(self, re_new_password):
        if re_new_password != self.initial_data['new_password']:
            raise serializers.ValidationError("两次输入密码不一致")

    def validate(self, attrs):

        new_password = self.initial_data['new_password']
        attrs["password"] = new_password
        del attrs["re_new_password"]
        del attrs["new_password"]
        return attrs

    class Meta:
        model = User
        fields = ("username", "password", "new_password","re_new_password")


