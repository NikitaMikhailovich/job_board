from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import get_user_model
from django import forms

User = get_user_model()


class UserCreateForm(UserCreationForm):
    
    user_type = forms.ChoiceField(choices=(('employer', 'employer'), ('job seeker', 'job seeker')))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'user_type')


class AuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')
