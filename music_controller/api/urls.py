from django.urls import path
from .views import main


# In our api.urls file indicated from [path('', include(api.url))], from music_container.urls
# We will import a function, (main), that we defined in our api.views file
urlpatterns = [
    # This urlpatterns array contains a:
    # path function that contains ("string", function main)
    path('home', main),
    # MEANING: If we get a url that is blank, path(''), then
    # call the function main from api.views and do whatever
    # the main function does which will return a HttpResponse("hello")

    path('', main),
    # This means we can have multiple paths
    # example: localhost:8000/api/home will call the main function
    # example: localhost:8000/api/ will call the main function as well
]


# localhost:8000/api/home
