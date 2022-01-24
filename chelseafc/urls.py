from django.urls import path
from .import views
urlpatterns = [
 path('1st/', views.samplefunction), 
 path('2nd/', views.londonfun)  
]
