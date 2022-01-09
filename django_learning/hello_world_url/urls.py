from django.urls import path

from . import views

app_name = "hello_url"
urlpatterns = [
    path('<str:username>', views.hello, name='user'),
]
