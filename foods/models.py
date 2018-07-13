from django.db import models
from django.contrib.auth.models import User

class Food(models.Model):
    brand = models.CharField(max_length=50)
    item = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

class Report(models.Model):
    owner = models.ForeignKey(User, related_name="reports",
                              on_delete=models.SET_NULL, null=True, blank=True)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    delayed_reaction = models.BooleanField()
    buildup_reaction = models.BooleanField()
    immediate_reaction = models.BooleanField()
    details = models.TextField(blank=True)
    company_response = models.TextField(blank=True)