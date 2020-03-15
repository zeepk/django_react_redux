from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('leadmanagerproject.frontend.urls')),
    path('', include('leadmanagerproject.leads.urls')),
    path('', include('leadmanagerproject.accounts.urls')),
]
