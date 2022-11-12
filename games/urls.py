from django.urls import path

from . import views

urlpatterns = [
    path('games/', views.home_view),
    path('lista/<int:id>', views.lista)
]