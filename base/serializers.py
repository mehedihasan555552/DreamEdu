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



class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields ='__all__'




class ApplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Apply
        fields ='__all__'




class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields ='__all__'




class EmailSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailSubscription
        fields = '__all__'