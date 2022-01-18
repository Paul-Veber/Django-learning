from django.urls import path

from . import views

app_name = "hello_form"
urlpatterns = [
    path('', views.get_guestbook, name='guestbook'),
]
