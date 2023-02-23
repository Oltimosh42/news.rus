from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .models import *
from .forms import *


class ShowArticles(ListView):
    model = Articles
    template_name = 'main/articles.html'
    context_object_name = 'art'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cat_selected'] = 0
        return context

    def get_queryset(self):
        return Articles.objects.order_by('-time_add')


class ShowPost(DetailView):
    model = Articles
    template_name = 'main/article_all.html'
    slug_url_kwarg = 'art_slug'
    context_object_name = 'art_all'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cat_selected'] = context['art_all'].cat_id
        return context


class ShowCategory(ListView):
    model = Category
    template_name = 'main/articles.html'
    context_object_name = 'art'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cat_selected'] = context['art'][0].cat_id
        return context

    def get_queryset(self):
        return Articles.objects.filter(cat__slug=self.kwargs['cat_slug'])


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация'
        return context


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'main/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Войти"
        return context

    def get_success_url(self):
        return reverse_lazy('articles')


def logout_user(request):
    logout(request)
    return redirect('login')
