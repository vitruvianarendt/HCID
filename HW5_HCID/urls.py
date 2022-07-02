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
    path('admin/', admin.site.urls),
    # url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
