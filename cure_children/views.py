from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.forms import UserCreationForm


class HomeView(LoginRequiredMixin, TemplateView):
    login_url = '/login'
    redirect_field_name = 'redirect_to'
    template_name = 'home.html'


class UserCreateView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = "/"

