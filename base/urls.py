from django.urls import path
from . import views


urlpatterns = [
    path('universitys/', views.getUniversitys, name='universitys'),
    path('universitys/<str:pk>/', views.getUniversity, name='university'),
    path('feedback/', views.getStudendFeedback, name='feedback'),
    path('solutions/', views.getStudySolutions, name='solutions'),


]