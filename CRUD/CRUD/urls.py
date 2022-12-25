"""CRUD URL Configuration

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
from ivy import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('task-list/', views.tasklist),
    path('task-detail/<int:pk>/', views.taskdetail),
    path('task-create/', views.taskcreate),
    path('task-update/<int:pk>/', views.taskupdate),
    path('task-delete/<int:pk>/', views.taskdelete),
    path('image-upload/', views.imageupload),
    path('image-update/<int:pk>/', views.imageupdate),

]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)