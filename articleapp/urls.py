from django.urls import path
from django.views.generic import TemplateView

from articleapp.view import ArticleCreateView, ArticleDetailView

from articleapp.views import ArticleUpdateView, ArticleDeleteView

app_name = 'articleapp'

urlpatterns = [
    path('list/', TemplateView.as_view(template_name='articleapp/list.html'), name='list'),
    path('create/', ArticleCreateView.as_view(), name='create'),
    path('detail/<int:pk>', ArticleDetailView.as_view(), name='detail'),
    path('update/<int:pk>', ArticleUpdateView.as_view(), name='detail'),
    path('delete/<int:pk>', ArticleDeleteView.as_view(), name='delete'),

]