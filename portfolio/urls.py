"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib.auth import views
from django.views.generic.base import RedirectView

from django.conf import settings
from django.conf.urls.static import static

import portfolios.forms

# from . import views

urlpatterns = [

                # path('portfolios/'), include('portfolios.urls', namespace='portfolios'),
                path('portfolios/', include('portfolios.urls')),
                # path('portfolios/', views.gallery, name='gallery'),
                # path('<slug>', portfolios.views.AlbumDetail.as_view(), name='album'),
                path('accounts/login/', views.LoginView, name='login'),
                path('logout', views.LogoutView, {'next_page': '/', }, name='logout'),
                path('admin/', admin.site.urls),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





