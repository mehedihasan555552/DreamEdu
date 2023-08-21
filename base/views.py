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



@api_view(['POST'])
def NewContact(request):
    data = request.data

    contact = Contact.objects.create(**data)

    serializer = ContactSerializer(contact, many=False)
    return Response(serializer.data)




@api_view(['POST'])
def ApplyNew(request):
    data = request.data
    first_name = data['first_name']
    last_name = data['last_name']
    applytype = data['applytype']
    address = data['address']
    city = data['city']
    country = data['country']
    passport = request.FILES['passport']
    photo = request.FILES['photo']
    police_clearance = request.FILES['police_clearance']
    bank_statement = request.FILES['bank_statement']
    stady_plan = request.FILES['stady_plan']
    higher_secondary = request.FILES['higher_secondary']
    other = request.FILES['other']

    apply = Apply.objects.create(first_name=first_name,last_name=last_name,applytype=applytype,address=address,city=city,country=country,passport=passport,photo=photo,police_clearance=police_clearance,bank_statement=bank_statement,stady_plan=stady_plan,higher_secondary=higher_secondary,other=other)

    serializer = ApplySerializer(apply, many=False)
    return Response(serializer.data)