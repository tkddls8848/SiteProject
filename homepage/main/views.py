from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('임시페이지입니다.')