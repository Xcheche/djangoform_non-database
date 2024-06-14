from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("success_page/", views.success_page, name="success_page"),  #  for succes_page
]
