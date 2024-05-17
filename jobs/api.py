from rest_framework import generics
from .models import Jobs, Company, Category
from .serializers import JobsListSerializer, JobsDetailSerializer, CompanySerializer, CategorySerializer


class JobsListAPI(generics.ListCreateAPIView):
    queryset = Jobs.objects.all()
    serializer_class = JobsListSerializer


class JobsDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Jobs.objects.all()
    serializer_class = JobsDetailSerializer

# ---------------

class CompanyListAPI(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CompanyDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


# ---------------

class CategoryListAPI(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



