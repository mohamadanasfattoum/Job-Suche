from rest_framework import generics
from .models import Jobs
from .serializers import JobsListSerializer, JobsDetailSerializer


class JobsListAPI(generics.ListCreateAPIView):
    queryset = Jobs.objects.all()
    serializer_class = JobsListSerializer


class JobsDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Jobs.objects.all()
    serializer_class = JobsDetailSerializer
