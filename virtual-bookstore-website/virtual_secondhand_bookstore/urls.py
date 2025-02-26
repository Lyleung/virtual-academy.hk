"""
URL configuration for virtual_secondhand_bookstore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

# from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views

from . import views

# import from local directory

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("", views.index, name="index"),
    path("", include('virtual_secondhand_bookstore.apps.public.urls')),
    # path("about", views.about, name="about"),
    # path("contact", views.contact, name="contact"),
    #     path('', TemplateView.as_view(template_name="index.html"), name="index"),
    path("accounts/", include('virtual_secondhand_bookstore.apps.accounts.urls')),
    # path("accounts/profile", views.ProfileView.as_view(), name="profile"),
    # Django Auth
    # path(
    #     "accounts/login",
    #     auth_views.LoginView.as_view(template_name="accounts/login.html"),
    #     name="login",
    # ),
    # # path('accounts/', include('django.contrib.auth.urls'))
    # path("accounts/logout", auth_views.LogoutView.as_view(), name="logout"),
#      we can create own app to these accounts
]
