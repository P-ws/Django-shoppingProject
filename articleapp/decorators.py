from django.contrib.auth.models import User
from django.http import HttpResponseForbidden


# 앞에 delete, update view에서 로그인만 했을때 method_decorator를 이용했고,
# 이 데코레이터는 요청한 유저가 그 pk에 맞는 유저일때는 진행하고, 아닐시 경고문뜨게 설정
from articleapp.models import Article


def article_ownership_required(func):
    def decorated(request, *args, **kwargs):
        article = Article.objects.get(pk=kwargs['pk'])
        if not article.writer == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)
    return decorated