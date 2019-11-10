"""note URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from django.views.generic.base import TemplateView
from note import views as core_views

urlpatterns = [
    path('admin/', admin.site.urls),
	path('accounts/', include('django.contrib.auth.urls')),
	path('', TemplateView.as_view(template_name='home.html'), name='home'),
	url(r'^signup/$', core_views.signup, name='signup'),
	url(r'^create/$', core_views.createpost, name='createpost'),
	url(r'display/$', core_views.display, name='display'),
	url(r'^delete-entry/(?P<pk>\d+)/$', core_views.DeleteView.as_view(), name='delete_view'),
]