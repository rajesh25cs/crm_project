from django.contrib import admin
from django.contrib import admin

admin.site.site_header = "SEPAL"
admin.site.site_title = "SEPAL Portal"
admin.site.index_title = "Welcome to SEPAL CRM"
# Register your models here.
from .models import Lead, Sale

admin.site.register(Lead)
admin.site.register(Sale)
