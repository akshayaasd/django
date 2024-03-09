# accounts/forms.py

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.utils.translation import gettext_lazy as _

class CustomUserCreationForm(UserCreationForm):
    error_messages = {
        'password_too_short': _("Your password must contain at least 8 characters."),
        'password_too_common': _("Your password is too common."),
    }

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields

class CustomAuthenticationForm(AuthenticationForm):
    error_messages = {
        'invalid_login': _("Please enter a correct username and password. Note that both fields may be case-sensitive."),
    }
