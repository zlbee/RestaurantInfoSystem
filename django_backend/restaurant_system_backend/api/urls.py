from django.urls import path, include
from . import views

urlpatterns = [
    # query the names of all the restaurants
    path('restaurant/query-all', views.query_restaurants),

    # query the detailed information of a specific restaurant according to the primary key
    path('restaurant/query-detail/<int:pk>', views.query_restaurant_detail),

    # add a restaurant record
    path('restaurant/add', views.add_restaurant),

    # update a restaurant record according to the primary key
    path('restaurant/delete/<int:pk>', views.delete_restaurant),

    # delete a restaurant record according to the primary key
    path('restaurant/update/<int:pk>', views.update_restaurant),

    # query restaurants according to filtering conditions
    path('restaurant/query-filtered/', views.query_filtered_restaurants_w_filterset),

    # query the names of all the restaurants with pagination
    path('restaurant/query-all-paged', views.query_restaurants_w_pagination),
]