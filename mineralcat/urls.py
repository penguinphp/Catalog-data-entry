from django.contrib import admin
from django.urls import path, include

from info import views

urlpatterns = [
    path('index/', views.home, name='home'),
    path('', views.home, name='name'),
    path('admin/', admin.site.urls),
    path('minerals/', include('info.urls')),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('group/<group_name>/', views.search_by_group, name='group')
]
