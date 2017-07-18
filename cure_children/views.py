from django.views.generic import TemplateView, CreateView
from django.contrib.auth.forms import UserCreationForm


class HomeView(TemplateView):
    template_name = 'index.html'


class UserCreateView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = "/"

