from django.shortcuts import render
#from basicapp.models import User
#from django.http import HttpResponse
from basicapp.forms import NewUserForm
# Create your views here.

def users(request):
    return render(request,'basicapp/users.html')

def index(request):

    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return users(request)
        else:
            print('ERROR FORM INVALID')
    return render(request,'basicapp/index.html',{'form':form})
