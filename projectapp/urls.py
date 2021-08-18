from django.urls import path

from projectapp.views import ProjectDetailView, ProjectCreateView, ProjectListView

app_name = 'projectapp'

urlpatterns = [
    path('detail/<int:pk>', ProjectDetailView.as_view(), name='detail'),
    path('create/', ProjectCreateView.as_view(), name='create'),
    path('list/', ProjectListView.as_view(), name='list'),

]