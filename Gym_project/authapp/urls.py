from django.urls import path
from . import views

urlpatterns = [
        path('',views.Home,name="Home"),
        path('signup',views.signup,name="signup"),
        path('login',views.handlelogin,name="handlelogin"),
        path('logout',views.handlelogout,name="handlelogout"),
]
