from django.urls import path
from . import views

app_name="trip"
urlpatterns=[
    path('', views.trip,name='trip'),
    path('ajax/Wchange/',views.Wchange,name='WChange'),
    path('trippost/', views.trippost,name='trippost'),
]
