from django.shortcuts import render

# Create your views here.
from HW5App.models import Course


def index(request):
    return render(request, "index.html")


def tech1(request):
    try:
        courses = Course.objects.all()
    except Course.DoesNotExist:
        courses = None

    context = {"courses": list(courses)}

    return render(request, "tech1.html",  context=context)


def tech2(request):
    try:
        courses = Course.objects.all()
    except Course.DoesNotExist:
        courses = None

    context = {"courses": list(courses)}

    return render(request, "tech2.html",  context=context)


def tech3(request):
    try:
        courses = Course.objects.all()
    except Course.DoesNotExist:
        courses = None

    context = {"courses": list(courses)}

    return render(request, "tech3.html",  context=context)


def chem1(request):
    try:
        courses = Course.objects.all()
    except Course.DoesNotExist:
        courses = None

    context = {"courses": list(courses)}

    return render(request, "chem1.html",  context=context)


def chem2(request):
    try:
        courses = Course.objects.all()
    except Course.DoesNotExist:
        courses = None

    context = {"courses": list(courses)}

    return render(request, "chem2.html",  context=context)


def chem3(request):
    try:
        courses = Course.objects.all()
    except Course.DoesNotExist:
        courses = None

    context = {"courses": list(courses)}

    return render(request, "chem3.html",  context=context)


def pal1(request):
    try:
        courses = Course.objects.all()
    except Course.DoesNotExist:
        courses = None

    context = {"courses": list(courses)}

    return render(request, "pal1.html",  context=context)


def pal2(request):
    try:
        courses = Course.objects.all()
    except Course.DoesNotExist:
        courses = None

    context = {"courses": list(courses)}

    return render(request, "pal2.html",  context=context)


def pal3(request):
    try:
        courses = Course.objects.all()
    except Course.DoesNotExist:
        courses = None

    context = {"courses": list(courses)}

    return render(request, "pal3.html",  context=context)


def space1(request):
    try:
        courses = Course.objects.all()
    except Course.DoesNotExist:
        courses = None

    context = {"courses": list(courses)}

    return render(request, "space1.html",  context=context)


def space2(request):
    try:
        courses = Course.objects.all()
    except Course.DoesNotExist:
        courses = None

    context = {"courses": list(courses)}

    return render(request, "space2.html",  context=context)


def space3(request):
    try:
        courses = Course.objects.all()
    except Course.DoesNotExist:
        courses = None

    context = {"courses": list(courses)}

    return render(request, "space3.html",  context=context)


def helppage(request):
    try:
        courses = Course.objects.all()
    except Course.DoesNotExist:
        courses = None

    context = {"courses": list(courses)}

    return render(request, "helppage.html",  context=context)


def contact(request):
    try:
        courses = Course.objects.all()
    except Course.DoesNotExist:
        courses = None

    context = {"courses": list(courses)}

    return render(request, "contact.html",  context=context)