from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from projectapp.models import Project


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscription', null=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='subscription', null=False)

    # user가 구독을 한번만 누를수있도록 엮어주기
    class Meta:
        unique_together = ['user', 'project']

    # 여기서 받아 저장하는 정보가없어서 따로 form은 안만들어준다.