from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request,"home.html",{})

def about(request):
	name = "HEllo world my name is arbaz khan"
	from pages.namer import namer
	return render(request,"about.html",{"name" : namer })
def contact(request):
	return render(request,"contact.html",{})