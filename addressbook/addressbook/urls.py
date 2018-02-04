"""addressbook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import include, url
import contacts.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', contacts.views.ListContactView.as_view(), name='contacts-list'),
    path('', contacts.views.CreateContactView.as_view(), name='contacts-new'),
    path('edit/<pk:int>/', contacts.views.updateContactView.as_view(), name='contacts-edit'),
    path('delete/<pk:int>/', contacts.views.DeleteContactView.as_view(), name='contacts-delete'),
    path('/<pk:int>/', contacts.views.ContactView.as_view(), name='contacts-view')
]
