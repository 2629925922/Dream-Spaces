from django.shortcuts import render
import csv
import os
from django.core.paginator import PageNotAnInteger,EmptyPage,Paginator

# Create your views here.

def load_file(name):
    data = []
    # dir = os.path.abspath(os.path.join(os.path.dirname('settings.py'),os.path.pardir))
    # dir = dir.replace("\\",'/')
    # aa = r"/static/images/TP/"+ name
    # files = os.path.join(dir,aa)
    files = r'C:\Users\Think\Desktop\文件\制梦空间 django项目\制梦空间\dreamspaces\static\images\TP\\'+name
    for file in os.listdir(files):
        data.append('/static/images/TP/'+ name +'/' + file)
    return data

def index(request,name='fj',page=1):
    data =  load_file(name)
    lists = Paginator(data,10)
    try:
        pages = lists.page(page)
    except PageNotAnInteger:
        pages = lists.page(1)
    except EmptyPage:
        pages = lists.page(lists.num_pages)
    return render(request,'bz.html',{"data":pages,"page_ranges":lists})



