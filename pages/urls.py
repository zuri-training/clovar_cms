from django.urls import path, include
from .views import HomePageView, DashboardView, selectTemplate, BloggerUsersView,viewTemplate

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("dashboard/", DashboardView.as_view(), name="dashboard"),
    path("dashboard/users/", BloggerUsersView.as_view(), name="users"),
    path("select_template/", selectTemplate, name="select_template"),
    path("select_template/<str:pk>/", viewTemplate, name="viewTemplate"),
]
