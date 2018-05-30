from django.urls import path
from . import views

app_name="REVIEW"
urlpatterns = [
    path('',views.reviewindex),
    path('comment/',views.reviewcomment,name="commenting"),
]
