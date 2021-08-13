from django.urls import path
from .views import *

urlpatterns = [
    path("create", CreateAPIView.as_view()),
    path("getPost", GetPostDataUsingId.as_view()),
    path("getAllPosts", getAmountPostData.as_view()),
    path("makeDonations", makeDonationsAPIView.as_view())
]