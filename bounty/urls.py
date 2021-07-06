from django.urls import path
from .views import CancelActiveBounty, CreateBounty, GetActiveBounty, GetBounties,StartBounty,StartActiveBounty, SubmitActiveBounty


urlpatterns = [
	path("create", CreateBounty.as_view()),
	path("get", GetBounties.as_view()),
	path("createActive",StartBounty.as_view()),
	path("getActive", GetActiveBounty.as_view()),
	path("cancelActive", CancelActiveBounty.as_view()),
	path("submitActive",SubmitActiveBounty.as_view()),
	path("startWorking", StartActiveBounty.as_view()),

    


]