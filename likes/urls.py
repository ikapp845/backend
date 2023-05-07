from django.urls import path
from . import views


urlpatterns = [
  path("",views.like,name = "Like"),
  path("asked/",views.asked_like,name = "Asked Like"),
  path("likes/<str:username>/",views.get_likes,name = "Get Likes"),
  path("friends_likes/<str:username>/",views.get_friends_likes,name = "Friends Likes")
]