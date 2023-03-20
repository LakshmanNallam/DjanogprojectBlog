from django.urls import path
from . import views

urlpatterns=[
    path("",views.home,name="home"),
    path("postsdetails/<slug:slug>/",views.postDetails,name="detailspage"),
    path("posts/",views.posts,name="postspage")
]