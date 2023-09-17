from django.db import models

class Membership(models.Model):
    membership_type = models.CharField(max_length=255)

    def __str__(self):
        return self.membership_type

class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    membership = models.ForeignKey(Membership, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"