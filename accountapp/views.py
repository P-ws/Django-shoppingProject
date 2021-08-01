from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

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
        #return render(requset, 'accountapp/middle.html', context={'hello_world_list': hello_world_list})
        #위의 방법으로 는 올때마다 post에서 수행 즉 새로고침 할때마다 그행동(쳤던내용저장)을 반복하기때문에 계속 추가되서 보임 그렇기떄문에 post가 한번
        #수행하게되면 get으로 되돌아가게해서 해결
        #HttpResposnseRedirect('account/base/')로 해도되지만 추후 편의를 위해 reverse함수를 사용
        #accountapp:base 는 account의 urls에 이름을 accountapp이라 하였고 거기에 경로의 이름을 base라 해두어서 이방법 가능
        #HttpResponseRedirect는 현재있는곳에서 다른곳으로 이동연결
        return HttpResponseRedirect(reverse('accountapp:base'))
    else:
        #get에서도 post처럼 보이기위해 설정
        #HelloWorld의 모델안에 객체들을 모두 꺼내어 변수로 할당(즉 여태form에 text친 내용들을 전부다 변수로 할당)

        hello_world_list = HelloWorld.objects.all()
        return render(requset, 'accountapp/middle.html', context={'hello_world_list': hello_world_list})


class AccountCreateView(CreateView):
    # User를 장고에서 받아와 모델로 설정
    model = User
    # UserCreationForm을 장고에서 받아와서 form
    form_class = UserCreationForm
    # class형 view에서는 reverse_lazy를 사용 함수형에서는 reverse를 사용
    success_url = reverse_lazy('accountapp:base')
    # 이 템플릿을 보여주기
    template_name = 'accountapp/create.html'


class AccountDetailView(DetailView):
    model = User
    #인스타로 따지면 다른사람이 나한테왔을때 내게시물들을 볼수있게 설정(detail.html에서 확인)
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'


class AccountUpdateView(UpdateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:base')
    template_name = 'accountapp/update.html'