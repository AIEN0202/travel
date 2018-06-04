from django.urls import path
from . import views

app_name="res"

urlpatterns = [
    path('',views.res),
    #localhost/res/res => booking.html
    path('booking/',views.booking),
    path('lightbox/',views.box)
]