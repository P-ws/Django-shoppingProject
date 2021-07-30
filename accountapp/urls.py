from django.urls import path

from accountapp.views import base


app_name='accountapp'

urlpatterns = [
    path('base/', base, name='hello_world'),
]