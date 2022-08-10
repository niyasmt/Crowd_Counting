from admn.models import RegisterdEvents
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterEventsForms(forms.ModelForm):
    class Meta:
        model = RegisterdEvents
        fields = ['name','email','phone']

class UserRegisterForm(UserCreationForm):
  email = forms.EmailField()

  class Meta:
      model = User
      fields = ['username', 'email', 'first_name', 'last_name']