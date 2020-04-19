#from .models import Customer
from django import forms



class CustomerForm(forms.Form):
	name = forms.CharField(label="Name",widget=forms.TextInput)
	Email = forms.EmailField(label="Email", widget = forms.EmailInput)
	password = forms.CharField(label="password",max_length=5,widget=forms.PasswordInput)
	choices = (("M","Male"),("F","Female"))
	sex = forms.ChoiceField(label="sex",choices=choices)
