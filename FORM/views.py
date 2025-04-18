from django.shortcuts import render,redirect
from .forms import RegistrationForm

def register(request):
    if request.method=="POST":
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            print("User registered succcessfully!")
            return redirect('login')
        else:
            print("form errors:",form.errors)
    else:
       form=RegistrationForm()
    return render(request, 'register.html', {'form': form})