from django.contrib.auth.models import Group
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView

from .forms import AuthenticationForm, UserCreateForm


class CreateUserView(CreateView):
    form_class = UserCreateForm
    template_name = 'account/create_user.html'
    success_url = '/'

    def form_valid(self, form):
        user = form.save()
        user_type = form.cleaned_data['user_type']
        group = Group.objects.get(name=user_type)
        user.groups.add(group)
        return super().form_valid(form)


class LoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'account/auth.html'
    success_url = '/'


class LogoutView(LogoutView):
    next_page = '/'
