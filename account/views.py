from django.shortcuts import render, redirect
from .forms import CreateUserForm 

def register(request):

    form = CreateUserForm()

    if request.method == 'POST':

        form = CreateUserForm(request.POST)

        if form.is_valid():

            form.save() #its like sending final post request

            return redirect('')

    context = {'form':form}



    return render(request, 'account/registration/register.html', context=context)