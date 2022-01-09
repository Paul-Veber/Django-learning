from django.urls import path

from . import views

app_name = "hello_form"
urlpatterns = [
    path('form', views.get_name, name='user'),
]
