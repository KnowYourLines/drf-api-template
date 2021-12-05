from django.urls import path

from api import views

urlpatterns = [
    path(r"example", views.ExampleView.as_view()),
]
