from . import views
from django.urls import path



urlpatterns = [
    path('',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('registration/',views.registration,name='registration'),
    path('about/',views.about,name='about'),
    path('home/',views.home,name='home'),
    
]


