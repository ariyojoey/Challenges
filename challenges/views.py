from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect


monthly_challenges = {
    "january": "Eat no meat for the rest of the month",
    "february": "Learn Django for at least an hour daily",
    "march": "Walk a little everyday",
    "april": "Learn Ruby at least twice weekly",
    "may": "Learn french daily",
    "june": "dance daily",
    "july": "teach weekly",
    "august": "dream big",
    "september": "swim",
    "october": "cook",
    "november": "steal person babe",
    "december": "use kingsley borrow money",
}

# Create your views here.


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    
    if month > len(months):
        return HttpResponseNotFound("Invalid Month!!!")
    
    redirect_month = months[month -1]
    return HttpResponseRedirect("/challenges/" + redirect_month)


def monthly_challenge(request, month):
    try:
      challenge_text = monthly_challenges[month]
      return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported!")

