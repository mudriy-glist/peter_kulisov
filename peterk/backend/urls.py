from django.urls import path

from . import views

urlpatterns = [path("", views.portfolio, name="portfolio"), path("message", views.message, name="message")]
