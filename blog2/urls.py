"""blog2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path

from posts.views import index, add_posts
from profiles.views import delivery, register, login_view, logout_view
from shop.views import shop_product

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('products/', shop_product, name='products'),
    path('delivery/', delivery, name='delivery'),
    path("register/", register, name="register"),
    path('addposts/', add_posts, name='add_posts'),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
]
