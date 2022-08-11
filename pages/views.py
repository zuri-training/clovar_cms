from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class HomePageView(TemplateView):
    template_name = "home.html"


class DashboardView(TemplateView):
    template_name = "dashboard.html"

#class choicepick(TemplateView):
    #template_name = "choose-url.html"
#def choicepick(request):
	#return render(request=request, template_name='choose-url.html')
#def signoutview(request):
	#return render(request=request, template_name='frontend/confirm-sign-out.html')
#def loginview(request):
	#return render(request=request, template_name='frontend/login.html')
#def newpage(request):
	#return render(request=request, template_name='frontend/new-page-desc.html')
#def pickniche(request):
	#return render(request=request, template_name='frontend/pick-niche.html')
#def signupview(request):
	#return render(request=request, template_name='frontend/signup-up.html')
#def verify_email(request):
	#return render(request=request, template_name='frontend/verify-email.html')