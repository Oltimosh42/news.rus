from django.urls import path
from .views import *

urlpatterns = [
    path('', ShowArticles.as_view(), name='articles'),
    path('articles/<slug:art_slug>/', ShowPost.as_view(), name='article_all'),
    path('category/<slug:cat_slug>/', ShowCategory.as_view(), name='category'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout')
]
