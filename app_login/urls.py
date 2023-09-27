from django.urls import path
from app_login import views
app_name = 'App_Login'



urlpatterns = [
    path('signup/', views.signup, name="signup")
]