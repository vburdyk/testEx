from rest_framework import serializers
from .models import Menu, Employee, Restaurant, Vote


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['name', 'app_version']


class RestaurantSerializer(serializers.ModelSerializer):
      class Meta:
        model = Restaurant
        fields = ['name']


class MenuSerializer(serializers.ModelSerializer):
    restaurant = RestaurantSerializer()
    class Meta:
        model = Menu
        fields = ['restaurant', 'date', 'items']


class VoteSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer()
    menu = MenuSerializer()
    class Meta:
        model = Vote
        fields = ['employee', 'menu', 'voted_at']
