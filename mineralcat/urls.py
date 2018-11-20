from django.contrib import admin
from django.urls import path, include

from info import views

urlpatterns = [
    path('index/', views.home, name='home'),
    path('', views.home, name='name'),
    path('admin/', admin.site.urls),
    path('minerals/', include('info.urls'))
]
