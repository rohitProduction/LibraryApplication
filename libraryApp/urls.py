"""
URL configuration for libraryApp project.

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
from django.urls import path
from books import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='homepage'),
    path('sign_up/', views.sign_up, name = 'sign_up'),
    path('log_in/', views.log_in, name='log_in'),
    path('libraryHome/', views.libraryHome, name='libraryHome'),
    path('bookList/', views.bookList, name='bookList'),
    path('bookDetails/<bookName>/', views.bookDetails, name='bookDetails'),
    path('borrow/<bookName>/', views.borrow, name='borrow'),
    path('logOut/', views.logOut, name='logOut'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
