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
from django.template.defaulttags import url
from django.urls import path, include, re_path

from HW5App.views import index

urlpatterns = [
    # path('/app/admin/', admin.site.urls),
    # path(r'^$', index, name="index"),
    #               # url(r'^$', 'views.home'),
    #               #
    # url(r'^admin/', include(admin.site.urls)),
   #// re_path(r'^$', index, name='index'),
    # re_path(r'^bio/(?P<username>\w+)/$', views.bio, name='bio'),
    # re_path(r'^blog/', include('blog.urls')),
    url(r'^$', 'index'),
    url(r'admin/', admin.site.urls)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



# urlpatterns = patterns('',
#     url(r'^$', 'index'),
#     url(r'^admin/', include(admin.site.urls)),
#     url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,}),
#
# )