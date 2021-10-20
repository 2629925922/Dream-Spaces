from django.shortcuts import render
import random
import requests
from django.shortcuts import HttpResponse
# Create your views here.

def index(request):
    return render(request,'transtions.html')


def fanyi(request,word):
    url = 'http://fanyi.youdao.com/translate?&doctype=json&type=AUTO&i='+word
    num = random.randint(1,3)
    headers1 = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'}
    headers2 = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
    headers3 = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36 Edg/89.0.774.75'}
    headers = eval('headers'+str(num))
    reponse = requests.get(url,headers=headers).json()
    return HttpResponse(reponse['translateResult'][0][0]['tgt'])