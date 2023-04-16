from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    is_Admin = models.BooleanField(default=False)
    is_Member = models.BooleanField(default=False)

class Expence(models.Model):
    Name  = models.CharField(max_length=140)
    Date_of_Expense = models.DateField()
    Category_CHOICES = (
        ("Health","Health"),
        ("Electronics", "Electronics"),
        ("Travel", "Travel"),
        ("Education", "Education"),
        ("Books", "Books"),
        ("Others", "Others")
         )
    Category = models.CharField(max_length=12,choices=Category_CHOICES,
        default='Health',
    )

    Description = models.TextField()
    Amount = models.PositiveIntegerField(null=True)
    Created_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True,default=None)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True)