from django.shortcuts import render
from django.views import generic
from .models import Jobs, Company, Category

class JobList(generic.ListView):
    model = Jobs

