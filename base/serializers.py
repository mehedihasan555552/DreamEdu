from rest_framework import serializers
from .models import *

class UniversityNameListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UniversityNameList
        fields ='__all__'




class StudentFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentsFeedback
        fields ='__all__'




class StudySolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudySolution
        fields ='__all__'