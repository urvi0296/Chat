from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from Chat.models import Message
from .forms import SendForm

def post_new(request):
    if request.method == "POST":
        form = SendForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.sender=request.user
            post.datetime = timezone.now()
            print(post.datetime)
            post.save()
            return redirect('/')
    else:
        form = SendForm()
    return render(request, 'post_edit.html', {'form': form})


def post_list(request):
    message = Message.objects.all().filter(reciever=request.user)
    return render(request, 'base.html',context={'message':message})
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})