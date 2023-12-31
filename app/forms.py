from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User,Event

class LoginForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )

class SignupForm(UserCreationForm):
    ROLES = [
        ('admin', 'Admin'),
        ('organizer', 'Organizer'),
        ('participant', 'Participant'),
    ]

    EVENTS = [
        ('singing', 'Singing'),
        ('dancing', 'Dancing'),
        # Add more events as needed
    ]

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
   
    user_role = forms.ChoiceField(choices=ROLES, required=True, label='Select Role', widget=forms.Select(attrs={"class": "form-control"}))
    event = forms.ModelChoiceField(queryset=Event.objects.all(), required=False, empty_label="Select Event", label='Select Event', widget=forms.Select(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'user_role', 'event',"event_list_user")
 


class EventForm(forms.ModelForm):
    event_list = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = Event
        fields = ("event_list",)


