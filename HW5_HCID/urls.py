"""HW5_HCID URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from HW5App.views import *

urlpatterns = [
    path('', index, name="index"),
    path('technology/basic/', tech1, name="tech1"),
    path('technology/intermediate/', tech2, name="tech2"),
    path('technology/advanced/', tech3, name="tech3"),
    path('chemistry/basic/', chem1, name="chem1"),
    path('chemistry/intermediate/', chem2, name="chem2"),
    path('chemistry/advanced/', chem3, name="chem3"),
    path('space/basic/', space1, name="space1"),
    path('space/intermediate/', space2, name="space2"),
    path('space/advanced/', space3, name="space3"),
    path('paleonthology/basic/', pal1, name="pal1"),
    path('paleonthology/intermediate/', pal2, name="pal2"),
    path('paleonthology/advanced/', pal3, name="pal3"),
    path('help/', helppage, name="helppage"),
    path('contact/', contact, name="contact"),
    path("register/", register_request, name="register"),
    path("login/", login_request, name="login"),
    path("logout/", logout_request, name="logout"),
    path('chemistry/basic/video/', chem1tutorial, name="chem1tutorial"),
    path('chemistry/intermediate/video/', chem2tutorial, name="chem2tutorial"),
    path('chemistry/advanced/video/', chem3tutorial, name="chem3tutorial"),
    path('space/basic/video/', space1tutorial, name="space1tutorial"),
    path('space/intermediate/video/', space2tutorial, name="space2tutorial"),
    path('space/advanced/video/', space3tutorial, name="space3tutorial"),
    path('technology/basic/video/', tech1tutorial, name="tech1tutorial"),
    path('technology/intermediate/video/', tech2tutorial, name="tech2tutorial"),
    path('technology/advanced/video/', tech3tutorial, name="tech3tutorial"),
    path('paleonthology/basic/video/', pal1tutorial, name="pal1tutorial"),
    path('paleonthology/intermediate/video/', pal2tutorial, name="pal2tutorial"),
    path('paleonthology/advanced/video/', pal3tutorial, name="pal3tutorial"),
    path('quiz/', quiz, name="quiz"),
    path('results/', results, name="results"),
    path('admin/', admin.site.urls),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
