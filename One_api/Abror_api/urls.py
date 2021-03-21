from django.urls import path
from . import views

urlpatterns=[
    path('article-list/',views.ArticleView.as_view(),name="article-list"),
    path('article-list/<int:article_id>/',views.ArticleView.as_view(),name='article-one'),
    path('article-update/<int:article_id>/',views.ArticleView.as_view(),name='article-update'),
    path('article-add/',views.ArticleView.as_view(),name='article-list'),
    path("author-list/",views.AuthorView.as_view(),name="author-list"),
    path("author-list/<int:id>/",views.ArticleView.as_view(),name='author-one'),
    path("author-update/<int:id>/",views.ArticleView.as_view(),name='author-update'),
    path("author-add/",views.ArticleView.as_view(),name='article-list')
]