from django.forms import ModelForm

from profileapp.models import Profile


# 장고에서 제공해주는 ModelForm을 적극 활용하여 ProfileCreationForm을 만들어줌
class ProfileCreationForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'nickname', 'message']