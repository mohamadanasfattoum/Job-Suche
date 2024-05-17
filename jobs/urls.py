from django.urls import path
from .views import JobList



urlpatterns = [

    path('', JobList.as_view()),
]