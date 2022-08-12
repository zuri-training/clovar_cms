from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class HomePageView(TemplateView):
    template_name = "home.html"


class DashboardView(TemplateView):
    template_name = "dashboard.html"

<<<<<<< HEAD
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
=======

class SelectTemplateView(TemplateView):
    template_name = "select_template.html"
>>>>>>> c21584273cec5dd633cf06d05650086e231280e7
