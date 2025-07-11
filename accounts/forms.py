from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, SetPasswordForm
from django import forms

from accounts.models import Profile

UserModel = get_user_model()

class AppUserCreationForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ['email','password1','password2']


        labels = {
            'email': 'Email',
            'password1': 'Password',
            'password2': 'Repeat Password'
        }


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Премахваме default help_text за паролите
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''

        # Задаваме placeholder-и директно тук:
        self.fields['email'].widget.attrs.update({
            'placeholder': 'Enter your email'
        })
        self.fields['password1'].widget.attrs.update({
            'placeholder': 'Enter your password'
        })
        self.fields['password2'].widget.attrs.update({
            'placeholder': 'Repeat your password'
        })


class AppUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = UserModel


# accounts/forms.py


class CustomSetPasswordForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['new_password1'].help_text = ''
        self.fields['new_password2'].help_text = ''



class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"

class CustomAuthenticationForm(AuthenticationForm):
    error_messages = {
        'invalid_login': '"Please enter a correct %(username)s and password.'

    }

class ProfileEditForm(ProfileBaseForm):
    pass

class ProfileCreateForm(ProfileBaseForm):

    ...

class ProfileDeleteForm(ProfileBaseForm):
    ...