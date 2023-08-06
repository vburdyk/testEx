from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    date = models.DateField()
    items = models.TextField()

    def __str__(self):
        return f"Menu for {self.restaurant.name} on {self.date}"


class Employee(models.Model):
    name = models.CharField(max_length=255)
    app_version = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Vote(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    voted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('employee', 'menu')

    def __str__(self):
        return f"{self.employee.name} voted for {self.menu.restaurant.name} on {self.menu.date}"
