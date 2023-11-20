from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Contact


def index(request):
    # Display contacts
    all_contacts = Contact.objects.all()

    return render(request, "index.html", {"contacts": all_contacts})
