from re import template
from django.conf import settings
from django.shortcuts import redirect
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *
# Create your views here.


class HomePageView(TemplateView):
    template_name = "home.html"


class DashboardView(TemplateView):
    template_name = "dashboard.html"


class BloggerUsersView(TemplateView):
    template_name = "dashboard_users.html"

def error_404(request, exception):
    return render(request, "404.html")

def selectTemplate(request):
    temp_name = Template.objects.all()
    context = {'temp_name':temp_name}
    return render(request, 'select_template.html',context)

def viewTemplate(request, pk):
    template = Template.objects.get(id=pk)
    return render(request, f'{template.directory}/{template.template_index}')
