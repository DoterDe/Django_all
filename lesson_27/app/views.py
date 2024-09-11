from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView
from .models import UserProfile
from django.urls import reverse_lazy
from .forms import CreatePostForm
from django.contrib.contenttypes.models import ContentType


def view(request):
    response = HttpResponse('qwerty')
    if 'counter' in request.COOKIES:
        cnt = int(request.COOKIES['counter']) +1
    else:
        cnt = 1
        response.set_cookie('counter', cnt)
    return response


def home(request):
    posts=UserProfile.objects.all()
    custom_attr = request.my_atribut_class


    return render(request, 'home.html', context= {'posts':posts , 'attr':custom_attr} )

class CreatePost(CreateView):
    model = UserProfile
    success_url = reverse_lazy('home')
    template_name = 'create.html'
    form_class = CreatePostForm

class DeletePost(DeleteView):
    model = UserProfile
    success_url = reverse_lazy('home')
    template_name = 'delete.html'
