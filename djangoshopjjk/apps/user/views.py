from django.shortcuts import render

# Create your views here.


from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
#from .models import User
from django.db.models import Q

User = get_user_model() # 如果

class CustomBackend(ModelBackend):
    """
    自定义用户验证
    """
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            #用户名和手机都能登录
            user = User.objects.get(
                Q(username=username) | Q(mobile=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


from django.shortcuts import render

# Create your views here.
