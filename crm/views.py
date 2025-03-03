from django.shortcuts import render
from . import views 
# Create your views here.

from .models import Lead

def lead_list(request):
    leads = Lead.objects.all()
    return render(request, 'crm/lead_list.html', {'leads': leads})
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')  # Ensure you have a home.html template
 # Incorrect import
# crm/views.py

from django.shortcuts import render

def crm_view(request):
    # Your logic for the CRM view
    return render(request, 'crm/crm_template.html')  # Ensure you have a template named 'crm_template.html'
from django.shortcuts import render, redirect
from .forms import LeadForm

def add_lead(request):
    if request.method == "POST":
        form = LeadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lead-list')
    else:
        form = LeadForm()
    
    return render(request, 'crm/add_lead.html', {'form': form})
