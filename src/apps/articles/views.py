from django.urls import reverse
from django.views.generic import DetailView, ListView, CreateView

from .forms import ArticleForm
from .models import Article, ArticleGallery


class ArticleListView(ListView):
    model = Article
    template_name = "index.html"
    context_object_name = "articles"

    def get_paginate_by(self, queryset=None):
        limit = self.request.GET.get("limit")
        return limit or 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["limit"] = self.get_paginate_by()
        return context


class ArticleCreateView(CreateView):
    model = Article
    template_name = "articles/article_create.html"
    form_class = ArticleForm

    def form_valid(self, form):
        self.object = form.save()
        images = self.request.FILES.getlist("images")
        for image in images:
            ArticleGallery.objects.create(article=self.object, image=image)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("articles:article_detail", kwargs={"pk": self.object.pk})


class ArticleDetailView(DetailView):
    model = Article
    template_name = "articles/article_detail.html"
