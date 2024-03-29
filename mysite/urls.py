"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from myapp import views as user_views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user_views.home, name='home'),
    path('signup/', user_views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name="users/login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name="users/logout.html"), name='logout'),
    path('history', TemplateView.as_view(template_name='public/history.html'), name='history'),
    path('quienes_somos', TemplateView.as_view(template_name='public/quienes_somos.html'), name='quienes_somos'),
    path('videos', user_views.videos, name='videos'),
    path('categorias', TemplateView.as_view(template_name='public/categorias.html'), name='categorias'),
    path('categorias2', user_views.categorias2, name='categorias2'),
    path('category/<pk>', user_views.CategoriaDetailView.as_view(), name='category-detail'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



