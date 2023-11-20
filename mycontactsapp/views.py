from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Contact


def index(request):
    contacts_list = Contact.objects.all().order_by("first_name", "last_name")

    formatted_list = "<br>".join(
        [f"{contact.first_name} {contact.last_name}" for contact in contacts_list]
    )

    centered_list = f'<div style="text-align: center;">{formatted_list}</div>'

    styled_response = (
        f"<style>body {{ background-color: #f0f0f0; }}</style>{centered_list}"
    )

    return HttpResponse("All Contacts:<br>" + styled_response)
