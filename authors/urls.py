from django.urls import path

from . import views

app_name = 'authors'

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('create/', views.register_create, name='register_create'),
    path('login/', views.login_view, name='login'),
    path('login/create/', views.login_create, name='login_create'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.games, name='home'),
    path('lists/', views.list_view, name='list_view'),
    path('lists/<int:id>/edit/', views.list_edit, name='list_edit'),
    # path('games/game/<int:id>', views.game_details, name='games_details'),
    path('favorites/', views.favorites_view, name='favorites'),
    path('favorites/<int:games_id>', views.favorites_add, name='favorites_add'),
]