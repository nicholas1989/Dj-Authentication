from django.shortcuts import render
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm

# Create your views here.
def home(request):
    return render(request, "index.html")


class SignupView(CreateView):
    form_class = CustomUserCreationForm
    success_url = '/accounts/login'
    template_name = 'registration/signup.html'
    
