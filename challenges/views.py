from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


def monthly_challenge(request, month):
    challenge_text = None
    if month == "january":
        challenge_text = "Eat no meat  fo the rest of the month"
    elif month == "february":
        challenge_text = "Learn Django for at least an hour daily"
    elif month == "march":
        challenge_text = "Walk a little everyday"
    else:
        return HttpResponseNotFound("This month is not supported!")
    return HttpResponse(challenge_text)
