from django.urls import path
from . import views

urlpatterns=[
    path('article-list/',views.ArticleView.as_view(),name="article_list"),
    path('article-list/int:article_id',views.ArticleView.as_view(),name='article-one'),
    path('article-update/int:article_id',views.ArticleView.as_view(),name='aricle-update'),
    path('article_add',views.ArticleView.as_view(),name='article-list')
]