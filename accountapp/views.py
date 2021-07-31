from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def base(requset):
    # get, post method 설정
    if requset.method == "POST":
        return render(requset, 'accountapp/middle.html', context={'text':'POST METHOD!!'})
    else:
        return render(requset, 'accountapp/middle.html', context={'text': 'GET METHOD!!'})