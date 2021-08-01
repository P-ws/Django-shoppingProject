from django.urls import path

app_name = 'profileapp'


urlpatterns = [
    path('profile/', admin.site.urls),
]
