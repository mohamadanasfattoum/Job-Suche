from django.urls import path
from .views import JobList, JobDetail
from .api import JobsListAPI, JobsDetailAPI, CompanyDetailAPI, CompanyListAPI



urlpatterns = [
    path('', JobList.as_view()),
    path('<slug:slug>', JobDetail.as_view()),


    path('list/', JobsListAPI.as_view()),
    path('list/<int:pk>', JobsDetailAPI.as_view()),
    path('companylist/', CompanyListAPI.as_view()),
    path('companylist/<int:pk>', CompanyDetailAPI.as_view()),




]