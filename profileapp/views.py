from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile


class ProfileCreateView(CreateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    success_url = reverse_lazy('accountapp:base')
    template_name = 'profileapp/create.html'

    #form_valid의 form은 forms의 애들을 받아오는거임(이것을 해주는 이유는 다른사람이 나의 이미지, 문구등을 바꿀수 있기때문에user을 매칭 시켜줌)
    def form_valid(self, form):
        #일단 임시로 nickname,message,image 들을 저장
        temp_profile = form.save(commit=False)
        # 유저라는 데이터가 아직 없어 temp_profile의 유저를 요청하는 유저로 설정
        temp_profile.user = self.request.user
        # 다 저장함
        temp_profile.save()
        return super().form_valid(form)