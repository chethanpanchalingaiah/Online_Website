from django.shortcuts import render
from django.http import HttpResponse
from .forms import CustomerForm


def signup(request):
	form = CustomerForm()
	return render(request,"shopping/signup.html",{'form':form})
def login(request):
	if request.method == "POST":
		if form.is_valid():
			return render(request,"shopping/signup.html",{'form':form})
	else:
		return HttpResponse("adsadsadsadd")



# Create your views here.
