from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .tasks import fetch_cat_fact


@api_view(["GET"])
def health_check(request):
    return Response({"healthy": "server healthy!!"})


@api_view(["GET"])
def fetch_fact(request):
    global last_fact
    task = fetch_cat_fact.delay()
    last_fact = task.get(timeout=5)
    return Response({"success": True})


@api_view(["GET"])
def get_fact(request):
    global last_fact
    if last_fact and "fact" in last_fact:
        return Response({"fact": last_fact["fact"]})
    else:
        return Response(
            {
                "error": "No task has been queued yet or there was an error fetching the fact"
            }
        )
