from django.urls import path

from accountapp.views import base, AccountCreateView

app_name='accountapp'

urlpatterns = [
    path('base/', base, name='base'),
    path('create/', AccountCreateView.as_view(), name='create'),
]