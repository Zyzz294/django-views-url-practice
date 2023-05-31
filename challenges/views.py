from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january": "Drink more water",
    "februrary": "go for a walk",
    "march": "go for a run",
    "april": "Drink more water",
    "may": "go for a walk",
    "june": "go for a run",
    "july": "Drink more water",
    "august": "go for a walk",
    "september": "go for a run",
    "october": "Drink more water",
    "november": "go for a walk",
    "december": "go for a walk"
}

# Create your views here.
def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months: 
        capitalized_month = month.capitalize()
        month_path = reverse("month_challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

        response_data = f"<ol>{list_items}</ol>"

    return HttpResponse(response_data)

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("404 error")
    redirect_month = months[month - 1]
    redirect_path = reverse("month_challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except: 
        return HttpResponseNotFound("<h1>404 error</h1>")