from django.shortcuts import render
from django.contrib.auth.views import LoginView,LogoutView

#Para el registro
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.urls import reverse_lazy


class UsersListView(LoginView):
  template_name="users/login.html"

#para que el boton cerrar sesion redirija a esa Url
class ClosedUser(LogoutView):
    next_page="list_products"

class RegisterView(generic.CreateView):
    form_class=UserCreationForm
    template_name="users/register.html"
    success_url=reverse_lazy("login")
