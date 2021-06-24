from django.urls import path
from .views import CreateBounty, GetActiveBounties, GetBounties,StartBounty,StartWorkingActive


urlpatterns = [
	path("create", CreateBounty.as_view()),
	path("get", GetBounties.as_view()),
	path("createActive",StartBounty.as_view()),
	path("getActive", GetActiveBounties.as_view()),

	path("startWorking", StartWorkingActive.as_view()),

    


]