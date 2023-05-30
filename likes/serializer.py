from rest_framework import serializers
from .models import Like
from group.serializers import ProfileSerializer



class LikeSerializer(serializers.ModelSerializer):
  question = serializers.SerializerMethodField("get_question")
  from_username = serializers.SerializerMethodField("get_fromuser")
  from_gender = serializers.SerializerMethodField("get_fromgender")
  username = serializers.SerializerMethodField("to_username")
  email = serializers.SerializerMethodField("to_email")

  class Meta:
    model = Like
    exclude = ["user_from","user_to"]


  def get_question(self,like):
    return like.question.question

  def get_fromuser(self,like):
    if like.user_to.paid == "True":
      if like.user_from.paid == "True":
        return "From user paid"
      else: 
        serializer = ProfileSerializer(like.user_from,many = False )
        return serializer.data
    else:
      return "To user not paid"

  def to_username(self,like):
    return like.user_to.name

  def to_email(self,like):
    return like.user_to.email

  def get_fromgender(self,like):
    return like.user_from.gender
 
 

class FriendLikeSerializer(serializers.ModelSerializer):
  question = serializers.SerializerMethodField("get_question")
  from_gender = serializers.SerializerMethodField("get_fromgender")
  username = serializers.SerializerMethodField("to_username")
  viewed = serializers.SerializerMethodField("to_viewed")

  class Meta:
    model = Like
    exclude = ["user_from","user_to","group","source","visited"]

  def to_viewed(self,like):
    return False

  def get_question(self,like):
    return like.question.question


  def to_username(self,like):
    return like.user_to.name

  def get_fromgender(self,like):
    return like.user_from.gender
