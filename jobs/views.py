from django.shortcuts import render
from django.views import generic
from .models import Jobs, Company, Category

class JobList(generic.ListView):
    model = Jobs



class JobDetail(generic.DetailView):
    model = Jobs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["company"] = Company.objects.get(jobs_company=self.get_object()) # to return data context["was man in template kommt"] jobs_company name Beziehung relationship
        return context







