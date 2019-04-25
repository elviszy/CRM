from django.conf.urls import url,include
from rest_framework.documentation import include_docs_urls
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.routers import DefaultRouter

from .views_op import AddUserView,UpdatePWDView
from SunFaLongCRM import views


router = DefaultRouter()
router.register(r'user',AddUserView,base_name='user')
router.register(r'custinfo',views.CustInfoModelView,base_name='custinfo')
router.register(r'updatepwd',UpdatePWDView,base_name='updatepwd')

urlpatterns = [
    url(r'docs/', include_docs_urls(title="zy")),
    url(r'^', include(router.urls)),
    url(r'^login/', obtain_jwt_token),
    # url(r'^register/$',AddUserView.as_view({"post":"create","get":"retrieve"})),
]
