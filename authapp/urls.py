from django.urls import path

from authapp.views import  CreateUser, Login, Profile, Logout

app_name='authapp'
urlpatterns = [

    path('login/', Login.as_view(), name='login'),
    path('register/', CreateUser.as_view(), name='register'),
    path('logout/', Logout.as_view(), name='logout'),
    path('profile/', Profile.as_view(), name='profile')
]