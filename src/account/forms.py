from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


User = get_user_model()


EMPLOYER = 'employer'
JOB_SEEKER = 'job seeker'

USER_TYPE_CHOICES = ((EMPLOYER, EMPLOYER), (JOB_SEEKER, JOB_SEEKER))

class UserCreateForm(UserCreationForm):
    
    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'user_type')


class AuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')
