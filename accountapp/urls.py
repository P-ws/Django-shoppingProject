from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accountapp.views import base, AccountCreateView, AccountDetailView, AccountUpdateView, AccountDeleteView

app_name='accountapp'

urlpatterns = [
    path('base/', base, name='base'),
    path('create/', AccountCreateView.as_view(), name='create'),
    # 로그인 로그아웃은 장고에서 제공해주는 클래스로 그냥 urls만 설정해주고 사용, 하지만 로그인은 보여줘야할 템플릿은 따로만들어주어야함
    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    # detail은 유저꺼를 보여줘야하기때문에 pk라는 이름의 int정보를 받겠다. 몇번유저에 접근할것인지
    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'),
    path('update/<int:pk>', AccountUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', AccountDeleteView.as_view(), name='delete'),

]