from django.shortcuts import render
from news.models import Column,Article
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('welcome to ')


def column_detail(request,column_slug):
    column = Column.objects.get(slug=column_slug)

    return render(request,'news/column.html',{'column':column})
    # return HttpResponse('column slug: '+column_slug)

def article_detail(request,article_slug):
    article = Column.objects.get(slug=article_slug)

    return render(request, 'news/article.html', {'article': article})
    # return HttpResponse('article slug'+article_slug)
