from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles':articles
    }
    return render(request, "articles/articles.html", context)

def article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    context = {
        'article':article
    }
    return render(request, "articles/article.html", context)
