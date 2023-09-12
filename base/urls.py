from django.urls import path
from . import views


urlpatterns = [
    path('universitys/', views.getUniversitys, name='universitys'),
    path('universitys/<str:pk>/', views.getUniversity, name='university'),
    path('feedback/', views.getStudendFeedback, name='feedback'),
    path('solutions/', views.getStudySolutions, name='solutions'),
    path('contact/', views.NewContact, name='contact'),
    path('apply/', views.ApplyNew, name='apply'),
    path('blogs/', views.Blogs, name='blogs'),
    path('blogs/<str:pk>/', views.getBlogs, name='blog'),
    path('latest-blogs/', views.LatestBlogs, name='latest-blogs'),
    path('newsletter/', views.Newsletter, name='newsletter'),
    path('members/', views.getTeamMember, name='members'),


]