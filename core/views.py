from django.shortcuts import render
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm

# Create your views here.
def home(request):
    return render(request, "index.html")


def SignupView(CreateView):
    form_class = CustomUserCreationForm
    success_url = '/login'
    template_name = 'signup.html'
    
