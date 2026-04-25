from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView
from .forms import CustomUserForm, CustomUserChangeForm
from .models import CustomUser
# Create your views here.

class RegisterView(CreateView):
    form_class = CustomUserForm
    template_name = "register.html"
    success_url = reverse_lazy("login")

class CustomLoginView(LoginView):
    template_name = "login.html"

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy("login")

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "user_board.html"

class CustomUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    template_name = "profile.html"
    success_url = reverse_lazy("dashboard")

    def get_object(self, queryset=None):
        return self.request.user