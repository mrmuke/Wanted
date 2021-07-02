from django.urls import path
from .views import CreateBounty, GetActiveBounty, GetBounties,StartBounty,StartActiveBounty


urlpatterns = [
	path("create", CreateBounty.as_view()),
	path("get", GetBounties.as_view()),
	path("createActive",StartBounty.as_view()),
	path("getActive", GetActiveBounty.as_view()),

	path("startWorking", StartActiveBounty.as_view()),

    


]