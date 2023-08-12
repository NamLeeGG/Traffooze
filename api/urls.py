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
  
    path('create-road-accident/', views.create_road_accident, name='create-road-accident'),
    path('view-road-accident/', views.view_road_accident, name='view-road-accident'),
    path('update-road-accident/', views.update_road_accident, name='update-road-accident'),
    path('delete-road-accident/', views.delete_road_accident, name='delete-road-accident'),
    path('search-road-accident/', views.search_road_accident, name='search-road-accident'),

]
