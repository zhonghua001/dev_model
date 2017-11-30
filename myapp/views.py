from django.shortcuts import render
from django.http import JsonResponse
from myapp.models import Column,Article
from django.http import HttpResponse

# Create your views here.

def index(request):
    columns = Column.objects.all()

    return render(request,'index.html',{'columns':columns})


def column_detail(request,column_slug):
    column = Column.objects.get(slug=column_slug)
    # column = column.article_set.objects.all()
    return render(request,'news/column.html',{'column':column})
    # return HttpResponse('column slug: '+column_slug)

def article_detail(request,article_slug):
    article = Article.objects.filter(slug=article_slug)

    return render(request, 'news/article.html', {'article': article,'article_slug':article_slug})
    # return HttpResponse('article slug'+article_slug)
#
def article_id_detail(request,article_slug,article_id):
    article = Article.objects.get(id=article_id)
    article_id = article.id
    article_title = article.title
    article_content = article.content
    data = {'article_id':article_id,'article_title':article_title,'article_content':article_content}
    return  JsonResponse(data)




def base(request):
    return render(request,'base.html')