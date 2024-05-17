from rest_framework import serializers
from .models import Jobs

class JobsListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =  Jobs
        fields = '__all__'


class JobsDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =  Jobs
        fields = '__all__'