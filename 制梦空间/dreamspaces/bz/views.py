from django.shortcuts import render,HttpResponse
import csv
import os
from django.core.paginator import PageNotAnInteger,EmptyPage,Paginator
from .models import Tk

# Create your views here.
def urls(name):
    url = r'C:\Users\Think\Desktop\文件\制梦空间 django项目\制梦空间\dreamspaces\static\images\TP\\' + name
    return url

def load_file(name):
    data = []
    # dir = os.path.abspath(os.path.join(os.path.dirname('settings.py'),os.path.pardir))
    # dir = dir.replace("\\",'/')
    # aa = r"/static/images/TP/"+ name
    # files = os.path.join(dir,aa)
    for file in os.listdir(urls(name)):
        data.append('/static/images/TP/'+ name +'/' + file)
    return data

def index(request,name='fj',page=1):
    data = Tk.objects.filter(url__icontains=name)
    # data =  load_file(name)
    lists = Paginator(data,12)
    try:
        pages = lists.page(page)
    except PageNotAnInteger:
        pages = lists.page(1)
    except EmptyPage:
        pages = lists.page(lists.num_pages)
    return render(request,'bz.html',{"data":pages,"page_ranges":lists})

def search(request):
    # names = ['bj','dm','fj','mn','mx','yx']
    # for name in names:
    #     for file in os.listdir(urls(name)):
    #         url = '/static/images/TP/'+ str(name) +'/' + str(file)
    #         data = Tk.objects.create(name=file,url=url)
    name = request.GET.get("tp_name")
    data = Tk.objects.filter(name__icontains=name)
    count = data.count()
    for i in data:
        print(i.url)
    return render(request,'bz_search.html',{'data':data,"count":count})

