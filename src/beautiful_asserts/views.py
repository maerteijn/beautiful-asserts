from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from .forms import ArticleForm
from .models import Article


class ArticleListView(ListView):
    model = Article
    fields = ("title",)


class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleForm
    success_url = reverse_lazy("article-list")
