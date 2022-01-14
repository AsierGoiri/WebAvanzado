from django.shortcuts import render
from django.contrib.auth  import authenticate, login, logout
from django.shortcuts import redirect, render
from django.core.checks import messages
from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic
from .forms import *
# Create your views here.

# Create your views here.
def Login(request):

    if request.user.is_authenticated:
        return redirect('Index')
    
   
    if request.method == 'POST':

        username=request.POST.get('username')
        password=request.POST.get('password')

        user = authenticate( request, username=username, password=password)


        if user is not None:
            login(request, user)
            return redirect('Index')
        else:
		   
            messages.warning(request, 'Usuario y/o contraseña incorrectas.''\n''Revise las mayúsculas, importan! \n Puede recuperar la contraseña si no se acuerda.')
            
           



    return render(request, 'login/login2.html')





class UserRegisterView(generic.CreateView):
		form_class = SignUpForm
		template_name = 'login/registro.html'
		success_url = reverse_lazy('Index')







class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'login/edit_user.html'
    success_url = reverse_lazy('Index')


    def get_object(self):
        return self.request.user