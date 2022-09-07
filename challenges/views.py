from audioop import reverse
from turtle import forward
from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.

monthly_challenges = {
    "january": "Eat no meat for the entire month",
    "february": "Walk for atleast 20 minutes every day",
    "march": "Learn django for atleast 20 minutes every day",
    "april": "Eat no meat for the entire month",
    "may": "Walk for atleast 20 minutes every day",
    "june": "Learn django for atleast 20 minutes every day",
    "july": "Eat no meat for the entire month",
    "august": "Walk for atleast 20 minutes every day",
    "september": "Learn django for atleast 20 minutes every day",
    "octobar": "Eat no meat for the entire month",
    "november": "Walk for atleast 20 minutes every day",
    "december": None
}

def index(request):
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {
      "months" : months
    })



def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text" : challenge_text,
            "month_name" : month
        }
        )
    except:
        raise Http404()
        # response_data = render_to_string("404.html")
        # return HttpResponseNotFound(response_data)
