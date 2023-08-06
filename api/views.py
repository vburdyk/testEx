from django.forms import model_to_dict
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from .models import Menu, Employee, Restaurant, Vote
from .serializers import MenuSerializer, EmployeeSerializer, RestaurantSerializer, VoteSerializer


class MenuAPIView(APIView):
    def get(self, request):
        menu = Menu.objects.all()
        serialized_menu = MenuSerializer(menu, many=True)
        return Response(serialized_menu.data)

    def post(self, request):
        restaurant_id = request.data.get('restaurant')
        new_menu = Menu.objects.create(
            restaurant=Restaurant.objects.get(id=restaurant_id),
            date=request.data['date'],
            items=request.data['items']
        )
        serialized_menu = MenuSerializer(new_menu)
        return Response(serialized_menu.data, status=status.HTTP_201_CREATED)


class MenuAPISingleView(APIView):
    def get_object(self, id):
        try:
            menu = Menu.objects.get(id=id)
            return menu
        except Menu.DoesNotExist:
            return None

    def get(self, request, id):
        menu = self.get_object(id)
        serialized_menu = MenuSerializer(menu)
        return Response(serialized_menu.data)

    def delete(self, request, id):
        menu = self.get_object(id)
        if menu is not None:
            menu.delete()
            return Response(None, status.HTTP_204_NO_CONTENT)
        return Response(None, status.HTTP_400_BAD_REQUEST)


class EmployeeView(APIView):

    def get(self, request):
        employee = Employee.objects.all()
        serialized_employee = EmployeeSerializer(employee, many=True)
        return Response(serialized_employee.data)

    def post(self, request):
        new_employee = Employee.objects.create(
            name=request.data['name'],
            app_version=request.data['app_version'],
        )
        serialized_employee = EmployeeSerializer(new_employee)
        return Response(serialized_employee.data, status=status.HTTP_201_CREATED)


class EmployeeSingleView(APIView):

    def get_object(self, id):
        try:
            employee = Employee.objects.get(id=id)
            return employee
        except Employee.DoesNotExist:
            return None

    def get(self, request, id):
        employee = self.get_object(id)
        serialized_employee = EmployeeSerializer(employee)
        return Response(serialized_employee.data)

    def delete(self, request, id):
        employee = self.get_object(id)
        if employee is not None:
            employee.delete()
            return Response(None, status.HTTP_204_NO_CONTENT)
        return Response(None, status.HTTP_400_BAD_REQUEST)


class RestaurantView(APIView):
    def get(self, request):
        restaurants = Restaurant.objects.all()
        serialized_restaurants = RestaurantSerializer(restaurants, many=True)
        return Response(serialized_restaurants.data)

    def post(self, request):
        new_restaurant = Restaurant.objects.create(
            name=request.data['name']
        )
        serialized_restaurants = RestaurantSerializer(new_restaurant)
        return Response(serialized_restaurants.data, status.HTTP_201_CREATED)


class RestaurantSingleView(APIView):
    def get_object(self, id):
        try:
            restaurant = Restaurant.objects.get(id=id)
            return restaurant
        except Restaurant.DoesNotExist:
            return None

    def get(self, request, id):
        restaurant = self.get_object(id)
        serialized_restaurant = RestaurantSerializer(restaurant)
        return Response(serialized_restaurant.data)

    def delete(self, request, id):
        restaurant = self.get_object(id)
        if restaurant is not None:
            restaurant.delete()
            return Response(None, status.HTTP_204_NO_CONTENT)
        return Response(None, status.HTTP_400_BAD_REQUEST)


class VoteView(APIView):
    def get(self, request):
        vote = Vote.objects.all()
        serialized_votes = VoteSerializer(vote, many=True)
        return Response(serialized_votes.data)

    def post(self, request):
        try:
            employee_id = request.data.get('employee')
        except Employee.DoesNotExist:
            return Response({"error": "Employee not found"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            menu_id = request.data.get('menu')
        except Menu.DoesNotExist:
            return Response({"error": "Menu not found"}, status=status.HTTP_400_BAD_REQUEST)

        new_vote = Vote.objects.create(
            employee=Employee.objects.get(id=employee_id),
            menu=Menu.objects.get(id=menu_id),
            voted_at=request.data['voted_at'],

        )
        serialized_vote = VoteSerializer(new_vote)
        return Response(serialized_vote.data, status.HTTP_201_CREATED)
