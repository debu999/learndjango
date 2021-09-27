# Create your views here.
import logging

from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import *

from .forms import ArticleModelForm
from .models import Article

logger = logging.getLogger(__name__)


class ArticleListView(ListView):
    template_name = "article_list.html"
    model = Article
    # queryset = Article.objects.all()


class ArticleDetailView(DetailView):
    template_name = "article_details.html"
    model = Article

    def get_object(self, *args, **kwargs):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)


class ArticleCreateView(CreateView):
    template_name = "article_create.html"
    form_class = ArticleModelForm
    model = Article

    # queryset = Article.objects.all() This is same as above line model=Article

    def form_valid(self, form):
        logger.info(form.cleaned_data)
        return super().form_valid(form)

    # add success_url = '/'
    # def get_success_url to send to some other page.


class ArticleUpdateView(UpdateView):
    template_name = "article_create.html"
    form_class = ArticleModelForm
    model = Article

    # queryset = Article.objects.all() This is same as above line model=Article

    def get_object(self, *args, **kwargs):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

    def form_valid(self, form):
        logger.info(form.cleaned_data)
        return super().form_valid(form)


class ArticleDeleteView(DeleteView):
    template_name = "article_delete.html"
    model = Article

    def get_object(self, *args, **kwargs):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

    def get_success_url(self):
        return reverse("articles:article_list")
