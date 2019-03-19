# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from .models import MylistTitle, MylistProduction, MylistGenre, MylistYear

# Create your views here.

def mainpage(request):
    return render(request, 'mylist/index.html')

def mylist(request):
    datas = MylistTitle.objects.all()
    return render(request, 'mylist/mylist.html', {'datas':datas})

def title_detail(request, title_slug):
    datas = get_object_or_404(MylistTitle, title_slug=title_slug)
    return render(request, 'mylist/title.html', {'datas':datas})

def production_list(request):
    datas = MylistProduction.objects.all()
    return render(request, 'mylist/productionlist.html', {'datas':datas})

def prodution_detail(request, production_slug):
    datas = get_object_or_404(MylistProduction, production_slug=production_slug)
    titles = MylistTitle.objects.all()
    related_titles = []

    for x in titles:
        if x.production == datas:
            related_titles.append(x)
        else:
            continue

    return render(request, 'mylist/production.html', {'datas':datas, 'titles':related_titles})

def genre_list(request):
    datas = MylistGenre.objects.all()
    return render(request, 'mylist/genrelist.html', {'datas':datas})

def genre_detail(request, genre_slug):
    datas = get_object_or_404(MylistGenre, genre_slug=genre_slug)
    titles = MylistTitle.objects.all()
    related_titles = []

    for x in titles:
        if x.genre1 == datas or x.genre2 == datas or x.genre3 == datas:
            related_titles.append(x)
        else:
            continue

    return render(request, 'mylist/genre.html', {'datas':datas, 'titles':related_titles})

def year_list(request):
    datas = MylistYear.objects.all()
    return render(request, 'mylist/yearlist.html', {'datas':datas})

def year_detail(request, year_slug):
    datas = get_object_or_404(MylistYear, year_slug=year_slug)
    titles = MylistTitle.objects.all()
    related_titles = []

    for x in titles:
        if x.year == datas:
            related_titles.append(x)
        else:
            continue

    return render(request, 'mylist/year.html', {'datas':datas, 'titles':related_titles})
