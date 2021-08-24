from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from articleapp.models import Article


class LikeRecord(models.Model):
    # cascade는 user가 삭제되었을때 같이 삭제됨
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='like_record', null=False)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='like_record', null=False)


    class Meta:
        unique_together = ['user' , 'article'] # 두개 연결되어있는 쌍이 유니크하다.
