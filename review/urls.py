from django.urls import path
from . import views

app_name="REVIEW"
urlpatterns = [
    path('',views.reviewindex,name="reviewindex"),
    # path('create/',views.create)
]
