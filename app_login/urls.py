from django.urls import path
from app_login import views

app_name = 'App_Login'



urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('change-profile/', views.user_change, name='user_change'),
    path('password/', views.pass_change, name='password'),
    path('add-profile-pic/', views.add_propic, name='add-profile-pic'),
    path('change-pro-pic/', views.change_pro_pic, name='change-pro-pic'),
]