from django.urls import path
from info import views


urlpatterns = [
    path('detail/<int:pk>/', views.detail, name='detail')
]

