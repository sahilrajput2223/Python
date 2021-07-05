from django.shortcuts import render, redirect
from . import models

# Create your views here.
def addUserDetails(request):
    temp = "addUser.html"
    if request.method == "POST":
        userName = request.POST.get('userName')
        email = request.POST.get('email')
        mobileNumber = request.POST.get('mobileNumber')
        address = request.POST.get('address')
        models.User.objects.create(userName = userName, email = email, mobileNumber = mobileNumber,address = address)
        return redirect("Home:allUser")
    else:
        return render(request, temp)


def allUser(request):
    temp = "showUser.html"
    data = models.User.objects.all()
    return render(request, temp, {'data':data})