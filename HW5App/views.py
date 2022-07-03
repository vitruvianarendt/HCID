from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

# Create your views here.
from HW5App.forms import NewUserForm
from HW5App.models import Course


def index(request):
    return render(request, "index.html")


def tech1(request):
    try:
        courses = Course.objects.all()
    except Course.DoesNotExist:
        courses = None

    context = {"courses": list(courses)}

    return render(request, "tech1.html", context=context)


def tech2(request):
    try:
        courses = Course.objects.all()
    except Course.DoesNotExist:
        courses = None

    context = {"courses": list(courses)}

    return render(request, "tech2.html", context=context)


def tech3(request):
    try:
        courses = Course.objects.all()
    except Course.DoesNotExist:
        courses = None

    context = {"courses": list(courses)}

    return render(request, "tech3.html", context=context)


def chem1(request):
    try:
        courses = Course.objects.all()
    except Course.DoesNotExist:
        courses = None

    context = {"courses": list(courses)}

    return render(request, "chem1.html", context=context)


def chem2(request):
    try:
        courses = Course.objects.all()
    except Course.DoesNotExist:
        courses = None

    context = {"courses": list(courses)}

    return render(request, "chem2.html", context=context)


def chem3(request):
    try:
        courses = Course.objects.all()
    except Course.DoesNotExist:
        courses = None

    context = {"courses": list(courses)}

    return render(request, "chem3.html", context=context)


def pal1(request):
    try:
        courses = Course.objects.all()
    except Course.DoesNotExist:
        courses = None

    context = {"courses": list(courses)}

    return render(request, "pal1.html", context=context)


def pal2(request):
    try:
        courses = Course.objects.all()
    except Course.DoesNotExist:
        courses = None

    context = {"courses": list(courses)}

    return render(request, "pal2.html", context=context)


def pal3(request):
    try:
        courses = Course.objects.all()
    except Course.DoesNotExist:
        courses = None

    context = {"courses": list(courses)}

    return render(request, "pal3.html", context=context)


def space1(request):
    try:
        courses = Course.objects.all()
    except Course.DoesNotExist:
        courses = None

    context = {"courses": list(courses)}

    return render(request, "space1.html", context=context)


def space2(request):
    try:
        courses = Course.objects.all()
    except Course.DoesNotExist:
        courses = None

    context = {"courses": list(courses)}

    return render(request, "space2.html", context=context)


def space3(request):
    try:
        courses = Course.objects.all()
    except Course.DoesNotExist:
        courses = None

    context = {"courses": list(courses)}

    return render(request, "space3.html", context=context)


def chem1tutorial(request):
    try:
        courses = Course.objects.all()
    except Course.DoesNotExist:
        courses = None

    context = {"courses": list(courses)}

    return render(request, "chem1tutorial.html", context=context)


def helppage(request):
    try:
        courses = Course.objects.all()
    except Course.DoesNotExist:
        courses = None

    context = {"courses": list(courses)}

    return render(request, "helppage.html", context=context)


def contact(request):
    try:
        courses = Course.objects.all()
    except Course.DoesNotExist:
        courses = None

    context = {"courses": list(courses)}

    return render(request, "contact.html", context=context)


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("index")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="register.html", context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("index")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("index")

