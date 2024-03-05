from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import UserCreateForm, AuthenticationForm
from django.contrib.auth.models import Group


class CreateUserView(CreateView):
    form_class = UserCreateForm
    template_name = 'account/create_user.html'
    success_url = '/'

    def form_valid(self, form):
        user = form.save(commit=False) # User(name='name', # только то что в форме)
        user_type = form.cleaned_data['user_type']
        group, _ = Group.objects.get_or_create(name=user_type)
        user.save()
        user.groups.add(group)
        # if user_type == 'employer':
        #     group, _ = Group.objects.get_or_create(name='Employers')
        #     user.save()
        #     user.groups.add(group)
        # elif user_type == 'job_seeker':
        #     group, _ = Group.objects.get_or_create(name='Job Seekers')
        #     user.save()
        #     user.groups.add(group)
        return super().form_valid(form)

class LoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'account/auth.html'
    success_url = '/'


class LogoutView(LogoutView):
    next_page = '/'