from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db import transaction
from .models import Like,AskedLike
from user.models import Profile
from question.models import Question
from .serializer import LikeSerializer,FriendLikeSerializer
from group.models import Members,Group,AskQuestion
from datetime import datetime
from django.db import transaction
from django.db.models import Count, Q, Value,F
from django.db.models.functions import Coalesce

@api_view(["POST"])
def like(request):
  req = request.data
  username1 = req["username1"]
  username2 = req["username2"]
  question_id = req["question"]
  profile_qs = Profile.objects.filter(email__in=[username1, username2])
  profiles = {profile.email: profile for profile in profile_qs}
  question = Question.objects.get(id=question_id)
  group = Group.objects.get(id = req["group"])
  members = Members.objects.filter(group = group)

  like = Like.objects.create(
      user_from=profiles[username1],
      user_to=profiles[username2],
      question=question,
      group=group,
  )
  profiles[username2].total_likes = profiles[username2].total_likes + 1
  profiles[username2].save()

  likes = Like.objects.filter(group=group, question=question)
  result = (
      likes.values('user_to__name')
      .annotate(count=Count('id'))
      .values('user_to__name', 'count')
  )

  total = sum(r['count'] for r in result)
  result = {"total": total, **{r['user_to__name']: {"count": r['count']} for r in result}}

  return Response(result)

@api_view(["POST"])
def asked_like(request):
  req = request.data
  username1 = req["username1"]
  username2 = req["username2"]
  question_id = req["question"]
  profile_qs = Profile.objects.filter(email__in=[username1, username2])
  profiles = {profile.email: profile for profile in profile_qs}
  question = AskQuestion.objects.select_related("group").get(id=question_id)
  members = Members.objects.filter(group=question.group)

  like = AskedLike.objects.create(
      user_from=profiles[username1],
      user_to=profiles[username2],
      question=question,
      group=question.group,
  )

  profiles[username2].total_likes = profiles[username2].total_likes + 1
  profiles[username2].save()

  likes = AskedLike.objects.filter(group=question.group, question=question)
  result = (
      likes.values('user_to__name')
      .annotate(count=Count('id'))
      .values('user_to__name', 'count')
  )


  total = sum(r['count'] for r in result)
  result = {"total": total, **{r['user_to__name']: {"count": r['count']} for r in result}}

  return Response(result)



@api_view(["GET"])
def get_likes(request,username):
  with transaction.atomic():
    user = Profile.objects.get(email = username)
    likes = Like.objects.filter(user_to=user).select_related('group', 'user_to',"question","user_from").order_by("-time")[:100]
  serializer = LikeSerializer(likes,many=True)

  return Response(serializer.data)


@api_view(["GET"])
def get_friends_likes(request,username):
  with transaction.atomic():
    user = Profile.objects.get(email = username)
    likes = Like.objects.filter(group__members__user=user).exclude(user_to = user).select_related('group', 'user_to',"question","user_from").order_by("-time")[:30]
  serializer = FriendLikeSerializer(likes,many=True)

  return Response(serializer.data)






# Create your views here.
