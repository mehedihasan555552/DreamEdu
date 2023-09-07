from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from .models import *
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail


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





@api_view(['GET'])
def Blogs(request):
    blogs = Blog.objects.all().order_by('-created_at')
    serializer = BlogSerializer(blogs, many=True)

    return Response({'blogs': serializer.data})




@api_view(['GET'])
def getBlogs(request, pk):
    blog = get_object_or_404(Blog, id=pk)
    serializer = BlogSerializer(blog, many=False)

    return Response({'blog': serializer.data})




@api_view(['GET'])
def LatestBlogs(request):
    blogs = Blog.objects.all().order_by('-created_at')[:3]
    serializer = BlogSerializer(blogs, many=True)

    return Response({'blogs': serializer.data})



@api_view(['POST'])
def Newsletter(request):
    data = request.data
    email = data['email']
    email_Subs = EmailSubscription.objects.create(email=email)
    if email_Subs:
        send_mail('Subscription Confirmation', 'Thank you for subscribing!', 'contact@dreameduifo.com', [email], fail_silently=True)

    serializer = EmailSubscriptionSerializer(email_Subs, many=False)
    return Response(serializer.data)









# import requests



# def facebookPost(request):
#     # Replace with your Page ID and App Secret Key
#     page_id = '1012236045619075'
#     app_secret_key = 'EAAY0zPZC0HxoBOwN3stXZBxE1mIo5xfWuiZCuusCXscqsuE6nHlslbpSZAL4CFOENCDp4s0ncZC15ZCLvZAvwJ1GyGIg9D9ryTaUsKZCZBwuDrijn8uWcPABYhtbjG8GvYUZBgTq4rCn69WbEEAWLe12TR6lDYGfj64nWAPjPwao6TKrrP1TZCrUNOpNcdAbZC2lxOnfRnFbZB4fVJab46SkP8LZBFdlS77QgZD'

#     # Generate a User Access Token using the App ID and App Secret Key
#     app_id = 'YOUR_APP_ID'
#     user_access_token_url = f'https://graph.facebook.com/oauth/access_token?client_id={app_id}&client_secret={app_secret_key}&grant_type=client_credentials'
#     response = requests.get(user_access_token_url)
#     access_token = response.json().get('access_token')

#     # Use the generated User Access Token to fetch posts
#     posts_url = f'https://graph.facebook.com/v12.0/{page_id}/posts?access_token={access_token}&fields=message,created_time'
#     response = requests.get(posts_url)

#     if response.status_code == 200:
#         data = response.json()
#         posts = data.get('data', [])
#         for post in posts:
#             message = post.get('message', 'No message')
#             created_time = post.get('created_time', 'No creation time')
#             print(f"Message: {message}\nCreated Time: {created_time}\n")
#     else:
#         print(f"Failed to fetch Facebook posts. Status code: {response.status_code}")

