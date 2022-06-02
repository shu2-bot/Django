#from django.http import HttpResponse
#from django.template import loader
#from django.shortcuts import render
from .models import Article
from django.views import generic
from .forms import ArticleForm
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(generic.ListView):
    model = Article
    template_name = 'index.html'

    def get_queryset(self):
        return Article.objects.order_by('-created_at')[:5]

class ArticleView(generic.DetailView):
    model = Article
    template_name = 'article.html'

class NewView(LoginRequiredMixin, generic.CreateView):
    form_class = ArticleForm
    template_name = 'form.html'
    success_url = '/'
    login_url = '/admin'

index = IndexView.as_view()
article = ArticleView.as_view()
new = NewView.as_view()

"""
def index(request):
    template = loader.get_template('index.html')
    articles = Article.objects.order_by('-created_at')[:5]   #「-」は新着順、無くすと古い順
    context = {
        'articles' : articles
    }
    return HttpResponse(template.render(context, request))

def page(request, page_id):
    message = 'ページ' + str(page_id)
    return HttpResponse(message)

def article(request, article_id):
    article = Article.objects.get(pk = article_id)
    template = loader.get_template('article.html')
    context = {
        'article' : article
    }
    return HttpResponse(template.render(context, request))
    #return render(request, 'article.html', context)   どちらでも可
"""