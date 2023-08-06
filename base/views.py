from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from .models import *
from django.shortcuts import get_object_or_404



# Create your views here.


@api_view(['GET'])
def getUniversitys(request):
    universitys = UniversityNameList.objects.all()
    serializer = UniversityNameListSerializer(universitys, many=True)

    return Response({'universitys': serializer.data})


@api_view(['GET'])
def getUniversity(request, pk):
    university = get_object_or_404(UniversityNameList, id=pk)
    serializer = UniversityNameListSerializer(university, many=False)

    return Response({'university': serializer.data})



@api_view(['GET'])
def getStudendFeedback(request):
    feedback = StudentsFeedback.objects.all()
    serializer = StudentFeedbackSerializer(feedback, many=True)

    return Response({'feedback': serializer.data})





@api_view(['GET'])
def getStudySolutions(request):
    feedback = StudySolution.objects.all()
    serializer = StudySolutionSerializer(feedback, many=True)

    return Response({'solutions': serializer.data})