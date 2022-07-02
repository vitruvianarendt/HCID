from django.shortcuts import render

# Create your views here.
from HW5App.models import Course


def index(request):
    try:
        course = Course.objects.get_queryset()
    except Course.DoesNotExist:
        course = None

    context = {"courses": course}

    return render(request, "index.html",  context=context)
