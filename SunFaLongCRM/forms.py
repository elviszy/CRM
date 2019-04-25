"""
bbs用到的form类
"""

from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
User = get_user_model()

# 定义一个注册的form类
class RegForm(forms.Form):

    name = forms.CharField(
        max_length=32,
        label="名称",
        error_messages={
            "max_length": "名称最长16位",
            "required": "名称不能为空",
        }
    )

    re_password = forms.CharField(
        min_length=6,
        label="确认密码",
        error_messages={
            "min_length": "确认密码至少要6位！",
            "required": "确认密码不能为空",
        }
    )



    def clean_username(self):
        username = self.cleaned_data.get("username")
        is_exist = User.objects.filter(username=username)
        if is_exist:
            # 表示用户名已注册
            self.add_error("username", ValidationError("用户名已存在"))
        else:
            return username
    # 重写全局的钩子函数，对确认密码做校验
    def clean(self):
        password = self.cleaned_data.get("password")
        re_password = self.cleaned_data.get("re_password")

        if re_password and re_password != password:
            self.add_error("re_password", ValidationError("两次密码不一致"))

        else:
            return self.cleaned_data


class ModifyPwdForm(forms.Form):
    password = forms.CharField(
        min_length=6,
        label="密码",
        error_messages={
            "min_length": "密码至少要6位！",
            "required": "密码不能为空",
        }
    )
    re_password = forms.CharField(
        min_length=6,
        label="确认密码",
        error_messages={
            "min_length": "确认密码至少要6位！",
            "required": "确认密码不能为空",
        }
    )

    def clean(self):
        password = self.cleaned_data.get("password")
        re_password = self.cleaned_data.get("re_password")

        if re_password and re_password != password:
            self.add_error("re_password", ValidationError("两次密码不一致"))

        else:
            return self.cleaned_data
