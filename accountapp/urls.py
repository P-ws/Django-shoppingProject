from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accountapp.views import base, AccountCreateView

app_name='accountapp'

urlpatterns = [
    path('base/', base, name='base'),
    path('create/', AccountCreateView.as_view(), name='create'),
    # 로그인 로그아웃은 장고에서 제공해주는 클래스로 그냥 urls만 설정해주고 사용, 하지만 로그인은 보여줘야할 템플릿은 따로만들어주어야함
    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

]