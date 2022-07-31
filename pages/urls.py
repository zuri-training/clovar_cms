from django.urls import path, include
from .views import HomePageView, DashboardView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("dashboard/", DashboardView.as_view(), name="dashboard"),
]
