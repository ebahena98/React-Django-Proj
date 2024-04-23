"""
URL configuration for music_controller project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Whatever web address you enter [indicated by path('') ]
    # Go into your api.urls file [indicated by path(include('api.urls'))]
    # Remeber to import the [include] function from django.urls
    path('api/', include('api.urls')),

    # path('api/', include('api.urls'))
    # localhost:8000/api/
    # whenever we get api/ , send the rest of the url
    # to api.urls then check inside the urlpatterns and
    # check if the path('example') is included in the url
    # localhost:8000/api/example
    # then if we see example, render the main function page

    path('', include('api.urls')),
]
