from django.db import models

class User(models.Model):
    user_types = (
        ('guest', 'Guest'),
        ('registered', 'Registered'),
        ('worker', 'Worker'),
        ('admin', 'Admin'),
    )
    
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    user_type = models.CharField(max_length=10, choices=user_types)

class UserPaymentInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    credit_card_number = models.CharField(max_length=16)

class Item(models.Model):
    categories = (
        ('t-shirt', 'T-shirt'),
        ('jeans', 'Jeans'),
        ('short', 'Short'),
        ('coat', 'Coat'),
        ('boot', 'Boot'),
    )

    genders = (
        ('male', 'Male'),
        ('female', 'Female'),
    )

    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=10, choices=genders)
    category = models.CharField(max_length=10, choices=categories)
    price = models.FloatField()
    brand = models.CharField(max_length=255)
    rating = models.FloatField()



class ItemOption(models.Model):
    colors = (
        ('red', 'Red'),
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('yellow', 'Yellow'),
        ('orange', 'Orange'),
        ('black', 'Black'),
        ('white', 'White'),
        ('pink', 'Pink'),
        ('purple', 'Purple'),
    )

    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    size = models.CharField(max_length=10)
    color = models.CharField(max_length=10, choices=colors)
    quantity = models.IntegerField()


class FavoriteItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)




