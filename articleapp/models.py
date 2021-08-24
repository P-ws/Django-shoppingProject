from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from projectapp.models import Project


class Article(models.Model):
    # 계정이 삭제되면 알수없는 계시물이라고 뜨게끔 설정
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='article', null=True)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, related_name='article', null=True)
    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='article/', null=False)
    content = models.TextField(null=True)
    #시간이 생성되었을때 자동으로 저장
    create_at = models.DateField(auto_now_add=True, null=True)

    like = models.IntegerField(default=0)