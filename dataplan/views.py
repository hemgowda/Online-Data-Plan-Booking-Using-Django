from django.shortcuts import render
from django.contrib.sessions.models import Session
Session.objects.all().delete()

# Create your views here.
from django.views import generic
from dataplan.models import Plan,Customer,Subscription


class PlanListView(generic.ListView):
    model = Plan
    template_name = 'plan_list.html'

class CustomerListView(generic.ListView):
    model = Customer
    template_name = 'customer_list.html'
