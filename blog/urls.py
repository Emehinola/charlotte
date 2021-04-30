from django.conf.urls import url
from . import views
from . views import ArticleList

urlpatterns = [
    url(r'category', views.category, name='category'),
    url(r'new-article', views.create_article, name='create-article'),
    url(r'(?P<link_title>.+)$', views.single_blog, name='single-blog'),
    # url(r'category/(?P<category>.+)$', views.category, name='category'),
    url(r'', ArticleList.as_view(), name='articles')
]
