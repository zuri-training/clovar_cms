from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class HomePageView(TemplateView):
    template_name = "home.html"


class DashboardView(TemplateView):
    template_name = "dashboard.html"


class SelectTemplateView(TemplateView):
    template_name = "select_template.html"
