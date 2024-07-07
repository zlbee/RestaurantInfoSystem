from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination

from .models import Restaurant
from .serializers import RestaurantSerializer, RestaurantNameSerializer
from .filters import RestaurantFilter

@api_view(['GET'])
def query_restaurants(request):
    """Query all the names of all the restaurants.

    Args:
        request (HttpRequest): Http request.

    Returns:
        HttpResponse: Http response, the names of the restaurants.
    """
    # names of all the restaurants
    all_restaurants_names = Restaurant.objects.all()

    # return results
    serializer = RestaurantNameSerializer(all_restaurants_names, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def query_restaurant_detail(request, pk):
    """Query the detailed information of a specific restaurant according to the primary key.

    Args:
        request (HttpRequest): Http request.
        pk(int): Primary key.

    Returns:
        HttpResponse: Http response.
    """
    # find the restaurant to be quried
    # if not found > return code 404
    target_restaurant = get_object_or_404(Restaurant, pk=pk)

    # return results
    serializer = RestaurantSerializer(target_restaurant)
    return Response(serializer.data)


@api_view(['POST'])
def add_restaurant(request):
    """Add a restaurant record.

    Args:
        request (HttpRequest): Http request that contains a restaurant record.

    Returns:
        HttpResponse: Http response.
    """
    # prepare the restaurant to be added
    serializer = RestaurantSerializer(data=request.data)

    # save record
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def update_restaurant(request, pk):
    """Update a restaurant record according to the primary key.

    Args:
        request (HttpRequest): Http request that contains a restaurant record.
        pk(int): Primary key.

    Returns:
        HttpResponse: Http response.
    """
    # prepare the record to be updated
    target_restaurant = Restaurant.objects.get(pk=pk)

    # record
    serializer = RestaurantSerializer(instance=target_restaurant, data=request.data)
    if serializer.is_valid():
        # save the record
        serializer.save()
        # return the updated record
        return Response(serializer.data)
    else:
        # return code 404
        return Response(status=status.HTTP_404_NOT_FOUND)
    

@api_view(['DELETE'])
def delete_restaurant(request, pk):
    """Delete a restaurant record according to the primary key.

    Args:
        request (HttpRequest): Http request.
        pk(int): Primary key.

    Returns:
        HttpResponse: Http response.
    """
    # find the restaurant to be deleted
    # if not found > return code 404
    restaurant = get_object_or_404(Restaurant, pk=pk)

    # delete target restaurant
    restaurant.delete()

    # return code 204
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def query_filtered_restaurants(request):
    """Query restaurants according to filtering conditions.

    Args:
        request (HttpRequest): Http request.

    Returns:
        HttpResponse: Http response, the filtered restaurants.
    """
    # retreive all restaurants
    all_restaurants = Restaurant.objects.all()

    # retreive query parameters
    param_location = request.query_params.get('location')
    param_cuisine = request.query_params.get('cuisine')

    # filter restaurants
    filtered_restaurants = all_restaurants
    if param_location:
        filtered_restaurants = Restaurant.objects.filter(location__icontains=param_location)

    if param_cuisine:
        filtered_restaurants = Restaurant.objects.filter(cuisine__icontains=param_cuisine)

    # return results
    serializer = RestaurantSerializer(filtered_restaurants, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def query_filtered_restaurants_w_filterset(request):
    """Query restaurants according to filtering conditions that filtering is implemented with the filterset.

    Args:
        request (HttpRequest): Http request.

    Returns:
        HttpResponse: Http response, the filtered restaurants.
    """
    # retreive all restaurants
    all_restaurants = Restaurant.objects.all()
    
    # construct the filterset
    filterset = RestaurantFilter(request.GET, queryset=all_restaurants)

    # filter restaurants
    if filterset.is_valid():
        filtered_restaurants = filterset.qs
    else:
        filtered_restaurants = all_restaurants

    # return response
    serializer = RestaurantSerializer(filtered_restaurants, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def query_restaurants_w_pagination(request):
    """Query all the names of all the restaurants with pagination.

    Args:
        request (HttpRequest): Http request.

    Returns:
        HttpResponse: Http response, the names of the restaurants with pagination.
    """
    # setup paginator
    paginator = PageNumberPagination()
    paginator.page_size = 3 # size of the page

    # names of all the restaurants with pagination
    all_restaurants = Restaurant.objects.all()
    all_restaurants_page = paginator.paginate_queryset(all_restaurants, request)

    # return results with pagination
    serializer = RestaurantNameSerializer(all_restaurants_page, many=True)
    return paginator.get_paginated_response(serializer.data)