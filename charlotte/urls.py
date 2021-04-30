"""charlotte URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from index import views as index_views
from blog import urls as blog_urls
from django.conf.urls.static import static
from django.conf import settings
from index.views import Home
from django.conf.urls import url
from blog import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include(blog_urls)),
    path('category/', views.category, name='category'),
    path('', Home.as_view(), name='home')
]  # setting urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)

# editing the default django texts
admin.site.site_header = "Daily Taste"
admin.site.site_title = "Daily Taste"
admin.site.index_title = "Daily Taste"
