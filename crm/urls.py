
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('crm/', views.crm_view, name='crm'),
]
