from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):
    # Profile에서 유저는 User모델과 연관되어있고, 이 User가 삭제되었을때 같이 삭제되어라는 CASCADE를 사용
    # request.user.profile (related_name 으로 profile로 연결)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(upload_to='profile/', null=True)
    nickname = models.CharField(max_length=20, unique=True, null=True)
    message = models.CharField(max_length=100, null=True)