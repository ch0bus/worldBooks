"""WebBooks URL Configuration

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

#urlpatterns = [
#    path('admin/', admin.site.urls),
#]


# Listing 8.2
from catalog import views
# Listing 9.9
# pip install django==3.2.10
#from django.conf.urls import url
# django.conf.urls.url() was deprecated in Django 3.0, and is removed in Django 4.0+.The easiest fix is to replace url() with re_path(). re_path uses regexes like url, so you only have to update the import and replace url with re_path.
from django.urls import re_path as url


urlpatterns = [
    #path('', views.index, name='home'),
    # Listing 10.27
    path('authors_add/', views.authors_add, name='authors_add'),
    # Listing 9.1
    path('', views.index, name='index'),    
    path('admin/', admin.site.urls),
    # Listing 10.32
    path('edit1/<int:id>/', views.edit1, name='edit1'),
    path('create/', views.create, name='create'),
    path('delete/<int:id>/', views.delete, name='delete'),

    # Listing 9.9    
    url(r'^books/$', views.BookListView.as_view(), name='books'),
    # В Django при использовании обобщенных классов получения данных доступ к со­ответствующей функции отображения информации 
    # организуется при помощи вы­зова метода as_view(). 
    # В результате выполняется вся запрограммированная работа по созданию экземпляра класса 
    # и гарантируется вызов правильных методов для входящих НТТР-запросов от пользователей.
    url(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
    # Listing 9.18
    url(r'^authors/$', views.AuthorListView.as_view(), name='authors'),
    
    
    #url('books/book_list/', views.BookListView.as_view(), name='books'),
]


# Listing 10.3
from django.urls import path, include
# Добавление URL-адреса для входа в систему
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]

# Listing 10.20
urlpatterns += [
    url(r'^mybooks/$', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
]


# Listing 10.38
urlpatterns += [
    url(r'^book/create/$', views.BookCreate.as_view(), name='book_create'),
    url(r'^book/update/(?P<pk>\d+)$', views.BookUpdate.as_view(), name='book_update'),
    url(r'^book/delete/(?P<pk>\d+)$', views.BookDelete.as_view(), name='book_delete'),
]

