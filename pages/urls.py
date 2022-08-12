from django.urls import path, include
<<<<<<< HEAD
from .views import HomePageView, DashboardView
#from .views import choicepick, signoutview, loginview, newpage, pickniche, signupview, verify_email

app_name="pages"
=======
from .views import HomePageView, DashboardView, SelectTemplateView
>>>>>>> c21584273cec5dd633cf06d05650086e231280e7

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("dashboard/", DashboardView.as_view(), name="dashboard"),
<<<<<<< HEAD
    #path("choose/", choicepick.as_view(), name="choose"),
    #path("choose/", choicepick, name="choose")
    

=======
    path("select_template/", SelectTemplateView.as_view(), name="select_template"),
>>>>>>> c21584273cec5dd633cf06d05650086e231280e7
]
