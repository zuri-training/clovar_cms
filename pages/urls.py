from django.urls import path, include
from .views import HomePageView, DashboardView, SelectTemplateView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("dashboard/", DashboardView.as_view(), name="dashboard"),
    path("select_template/", SelectTemplateView.as_view(), name="select_template"),
]
