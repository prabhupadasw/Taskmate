# users_app/views.py

from django.shortcuts import render ,redirect
from  users_app.forms import CustomRegisterForm
from django.contrib import messages
def register(request):
    if request.method =="POST":
        register_form = CustomRegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request,("New User Account Created,Login to get Started"))
            return redirect('register')
    

    else:
        register_form = CustomRegisterForm()
    return render(request, "register.html", {'register_form': register_form})

