from rest_framework import serializers
from .models import Jobs , Company, Category

class JobsListSerializer(serializers.ModelSerializer):
    company= serializers.StringRelatedField()
    category= serializers.StringRelatedField()
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



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model =  Category
        fields = '__all__'