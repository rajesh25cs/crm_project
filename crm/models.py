from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Lead(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    status = models.CharField(max_length=50, choices=[('New', 'New'), ('Contacted', 'Contacted'), ('Converted', 'Converted')])
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Sale(models.Model):
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE)
    sale_amount = models.DecimalField(max_digits=10, decimal_places=2)
    sale_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[('Pending', 'Pending'), ('Closed', 'Closed')])

    def __str__(self):
        return f"Sale - {self.lead.name} - {self.sale_amount}"
