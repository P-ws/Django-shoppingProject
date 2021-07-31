from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from accountapp.models import HelloWorld


def base(requset):
    # get, post method 설정
    if requset.method == "POST":
        # POST라는 메서드에서 괄호안에 있는 이름을 가진애를 가져와라.
        temp = requset.POST.get('hello_world_input')
        # HelloWorld는 우리가 만든 모델을 변수
        # 그리고 form에 text를 적어 불러오는 temp라는 애를 모델안에 설정한 변수 text에 넣어줌
        # 바로 데이터 베이스에 저장
        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()

        # 저장된 데이터객체를 내보내주는역할
        return render(requset, 'accountapp/middle.html', context={'hello_world_output':new_hello_world})
    else:
        return render(requset, 'accountapp/middle.html', context={'text': 'GET METHOD!!'})