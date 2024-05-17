from rest_framework import serializers
from .models import Jobs , Company

class JobsListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =  Jobs
        fields = '__all__'


class JobsDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =  Jobs
        fields = '__all__'



class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model =  Company
        fields = '__all__'