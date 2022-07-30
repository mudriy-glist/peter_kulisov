from django.shortcuts import render
from backend.models import Message
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def portfolio(request):
    return render(request, "backend/portfolio.html")

def message(request):
    if request.method == "POST":

        name = request.POST["name"]
        email = request.POST["email"]
        phone_number = request.POST["phone_number"]
        message = request.POST["message"]
        message_data = Message(name=name, email=email, phone_number=phone_number, message=message)
        message_data.save()
    return HttpResponseRedirect(reverse("portfolio"))