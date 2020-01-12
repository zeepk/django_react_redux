from django.urls import path
from . import views


urlpatterns = [
    # from the root directory, load the index view
    path('', views.index)
]
