from django.urls import path
from . import views

app_name="member"
urlpatterns = [
    path('', views.index, name="index"),
    path('signup/', views.signup, name="signup"),
    path('login/', views.login, name="login"),
    path('mReg/', views.mReg, name="mReg"),
    path('Main_index/', views.Main_index, name="Main_index"),
]