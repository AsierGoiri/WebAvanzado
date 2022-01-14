from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms


class SignUpForm(UserCreationForm):
    username =  forms.CharField(max_length=100, widget=forms.TextInput(
	    attrs={'class': 'form-control ', 'placeholder': 'ejemplo14'}))
    email = forms.EmailField(widget=forms.EmailInput(
	    attrs={'class': 'form-control', 'placeholder': 'ejemplo@gmail.com'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(
	    attrs={'class': 'form-control ', 'placeholder': 'Indica tu nombre'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(
	    attrs={'class': 'form-control ', 'placeholder': 'Indica tu apellido'}))

    password1 = forms.CharField(widget = forms.PasswordInput(render_value = True, attrs={'class': 'form-control', 'placeholder': '********'}))
    password2 = forms.CharField(widget = forms.PasswordInput(render_value = True, attrs={'class': 'form-control', 'placeholder': '********'}))
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        # widgets = {
        # 'password1': forms.PasswordInput(attrs={'class':'form-control'}),
        # 'password2': forms.PasswordInput(attrs={'class':'form-control'}),
        # }



class EditProfileForm(UserChangeForm):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control ', 'placeholder': 'Set your first name...'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control '}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control ', 'placeholder': 'Set your first name...'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control ', 'placeholder': 'Set your last name...'}))
   

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')
