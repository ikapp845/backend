from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
  path("post/",views.post,name = "Post"),
  path("update_image/",views.update_image,name = "Update image"),
  path("check_username/<str:email>/",views.check_username,name = "Check Username"),
  path("delete_account/<str:username>/",views.delete_account,name = "Delete Account"),
  path("login/<str:mail>/",views.login,name = "Login"),
  path("check_mail/<str:mail>/",views.check_email,name = "Check Mail"),
  path("check_otp/<str:email>/<str:otp>/",views.check_otp,name = "Check OTP"),
  path("get_contacts/",views.get_contacts,name = "Get Contacts"),
  path("get_group_contacts/",views.get_group_contacts,name = "Get Group Contacts"),
  path("delete_account/<str:email>/",views.delete_account,name = "Delete Account"),
  path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]