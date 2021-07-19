from django.urls import path
from .views import ApproveActiveBounty, CancelActiveBounty, CreateBounty, DenyActiveBounty, GetActiveBounty, GetAwaitingApproval, GetBounties,StartBounty,StartActiveBounty, SubmitActiveBounty


urlpatterns = [
	path("create", CreateBounty.as_view()),
	path("get", GetBounties.as_view()),
	path("createActive",StartBounty.as_view()),
	path("getActive", GetActiveBounty.as_view()),
	path("getAwaiting", GetAwaitingApproval.as_view()),
	path("cancelActive", CancelActiveBounty.as_view()),
	path("submitActive",SubmitActiveBounty.as_view()),
	path("startWorking", StartActiveBounty.as_view()),
	path("deny/<int:id>",DenyActiveBounty.as_view()),
	path("accept/<int:id>", ApproveActiveBounty.as_view()),

    


]