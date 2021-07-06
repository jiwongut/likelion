from django.djangoproject2.blogproject.account.views import login_view, register_view
from django.urls import path
from blog.views import *

urlpatterns = [
    path('login/',login_view,name="login"),
    path('logout/',login_view,name="logout"),
    path('register/',register_view,name="signup")
]