from django.urls import path
from . import views

urlpatterns = [
    path('category/list/', views.CategoryView.as_view(), name='category-list'),
    path('category/<int:pk>/', views.CategoryView.as_view(), name='article-one'),
    path('category/add/', views.CategoryView.as_view(), name='article-add'),
    path('category/<int:pk>/update/', views.CategoryView.as_view(), name='article-update'),
    path('category/<int:pk>/delete/', views.CategoryView.as_view(), name='article-update'),
]