from django.urls import path, include
from .views import HomePageView, DashboardView
#from .views import choicepick, signoutview, loginview, newpage, pickniche, signupview, verify_email

app_name="pages"

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("dashboard/", DashboardView.as_view(), name="dashboard"),
    #path("choose/", choicepick.as_view(), name="choose"),
    #path("choose/", choicepick, name="choose")
    

]
