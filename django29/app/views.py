from .models import Author
from .forms import SignUpForm
from django.views.generic import CreateView
from django.urls import reverse_lazy



class SignUpView(CreateView):


    model = Author
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'