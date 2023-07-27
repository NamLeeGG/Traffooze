from django.urls import path
from api import views

urlpatterns = [
    path('', views.getUserAccount, name='get-user-account'),

    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register_account, name='register'),
    
    path('create-traffic-jam/', views.create_traffic_jam, name='create-traffic-jam'),
    path('view-traffic-jam/', views.view_traffic_jam, name='view-traffic-jam'),
    path('update-traffic-jam/', views.update_traffic_jam, name='update-traffic-jam'),
    path('delete-traffic-jam/', views.delete_traffic_jam, name='delete-traffic-jam'),
    path('search-traffic-jam/', views.search_traffic_jam, name='search-traffic-jam'),

    path('create-road-closure/', views.create_road_closure, name='create-road-closure'),
    path('view-road-closure/', views.view_road_closure, name='view-road-closure'),
    path('update-road-closure/', views.update_road_closure, name='update-road-closure'),
    path('delete-road-closure/', views.delete_road_closure, name='delete-road-closure'),
    path('search-road-closure/', views.search_road_closure, name='search-road-closure'),
]
