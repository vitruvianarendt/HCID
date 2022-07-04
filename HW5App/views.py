from random import randint

from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

# Create your views here.
from HW5App.forms import NewUserForm, QuizForm
from HW5App.models import Course, Quiz


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


def tech1tutorial(request):
    try:
        courses = Course.objects.all()
    except Course.DoesNotExist:
        courses = None

    context = {"courses": list(courses)}

    return render(request, "tech1tutorial.html", context=context)


def tech2tutorial(request):
    try:
        courses = Course.objects.all()
    except Course.DoesNotExist:
        courses = None

    context = {"courses": list(courses)}

    return render(request, "tech2tutorial.html", context=context)


def tech3tutorial(request):
    try:
        courses = Course.objects.all()
    except Course.DoesNotExist:
        courses = None

    context = {"courses": list(courses)}

    return render(request, "tech3tutorial.html", context=context)


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


def pal1tutorial(request):
    try:
        courses = Course.objects.all()
    except Course.DoesNotExist:
        courses = None

    context = {"courses": list(courses)}

    return render(request, "pal1tutorial.html", context=context)


def pal2tutorial(request):
    try:
        courses = Course.objects.all()
    except Course.DoesNotExist:
        courses = None

    context = {"courses": list(courses)}

    return render(request, "pal2tutorial.html", context=context)


def pal3tutorial(request):
    try:
        courses = Course.objects.all()
    except Course.DoesNotExist:
        courses = None

    context = {"courses": list(courses)}

    return render(request, "pal3tutorial.html", context=context)


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


def space1tutorial(request):
    try:
        courses = Course.objects.all()
    except Course.DoesNotExist:
        courses = None

    context = {"courses": list(courses)}

    return render(request, "space1tutorial.html", context=context)


def space2tutorial(request):
    try:
        courses = Course.objects.all()
    except Course.DoesNotExist:
        courses = None

    context = {"courses": list(courses)}

    return render(request, "space2tutorial.html", context=context)


def space3tutorial(request):
    try:
        courses = Course.objects.all()
    except Course.DoesNotExist:
        courses = None

    context = {"courses": list(courses)}

    return render(request, "space3tutorial.html", context=context)


def chem1tutorial(request):
    try:
        courses = Course.objects.all()
    except Course.DoesNotExist:
        courses = None

    context = {"courses": list(courses)}

    return render(request, "chem1tutorial.html", context=context)


def chem2tutorial(request):
    try:
        courses = Course.objects.all()
    except Course.DoesNotExist:
        courses = None

    context = {"courses": list(courses)}

    return render(request, "chem2tutorial.html", context=context)


def chem3tutorial(request):
    try:
        courses = Course.objects.all()
    except Course.DoesNotExist:
        courses = None

    context = {"courses": list(courses)}

    return render(request, "chem3tutorial.html", context=context)


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


def quiz(request):
    if request.method == "POST":
        form_data = QuizForm(data=request.POST, files=request.FILES)
        if form_data.is_valid():
            post = form_data.save(commit=False)
            post.user = request.user
            post.points = randint(40, 100)
            post.save()
            return redirect("results")
    list1 = request.META.get('HTTP_REFERER')
    url=''
    if list1 is not None:
        list2 = list1.split('/')
        n = 3
        newlist = list2[n:]
        url = ''.join(newlist)

    context = {"quiz": QuizForm, "url": url}
    return render(request, "quiz.html", context=context)


def results(request):
    try:
        all_quizzes = Quiz.objects.filter(user=request.user)
    except Quiz.DoesNotExist:
        all_quizzes = None

    context = {"quizzes": all_quizzes}
    return render(request, "results.html", context=context)
