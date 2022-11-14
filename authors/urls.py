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
    path('lists/', views.list_view, name='lists'),
    path('lists/<int:id>/edit/', views.list_edit, name='list_edit'),
    path('mylists/', views.my_list, name='my_list'),
    # path('games/game/<int:id>', views.game_details, name='games_details'),
    path('favorites/', views.favorites_view, name='favorites'),
    path('favorites/<int:games_id>', views.favorites_add, name='favorites_add'),
    # path('newlist/', views.newlist_view, name='newlist'),
    path('newlist/add', views.newlist_add, name='newlistadd'),
    path('addgame/', views.addgame, name='addgame'),
    path('delete/<int:games_id>', views.delete_item, name='delete_item'),
    path('details/<int:id>', views.game_details, name='game_details'),
    path('game/<int:id>', views.details, name='details'),
    path('listdetail/<int:id>', views.lists_details, name='listdetail'),

    # path('review/<int:games_id>', views.submit_review, name='review'),



]