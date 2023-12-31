from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import SignupForm, LoginForm,EventForm
from .models import User

def index(request):
    return render(request, 'index.html')

def register(request):
    return render(request, 'register.html')

def register_organizer(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        event_form = EventForm(request.POST)
        if form.is_valid() and event_form.is_valid():
            user = form.save(commit=False)
            user.is_admin = form.cleaned_data['user_role'] == 'admin'
            user.is_organizer = form.cleaned_data['user_role'] == 'organizer'
            user.is_participant = form.cleaned_data['user_role'] == 'participant'
            user.event = form.cleaned_data['event']
            user.event_list_user = event_form.cleaned_data['event_list']
            user.save()

            event = event_form.save(commit=True)
            event.user = user
            event.event_list = event_form.cleaned_data['event_list']  # Access 'event_list' from the event_form
            event.save()

            return redirect('login_view')  # Replace 'login_view' with your login page URL or name
    else:
        form = SignupForm()
        event_form = EventForm()

    return render(request, 'register.html', {'form': form, 'event_form': event_form})
def registeradmin(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            admin = form.save(commit=False)
            admin.is_admin = True
            admin.save()
            return redirect('login_view')
    else:
        form = SignupForm()

    return render(request, 'register.html', {'form': form})

def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None

    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_admin:
                    login(request, user)
                    return redirect('adminpage')
                elif user.is_organizer:
                    login(request, user)
                    return redirect('organizer')
                elif user.is_participant:
                    login(request, user)
                    return redirect('participant')
            else:
                msg = 'Invalid username or password'
        else:
            msg = 'Error validating form'

    return render(request, 'login.html', {'form': form, 'msg': msg})

def admin(request):
    return render(request, 'admin.html')

def organizer(request):
    return render(request, 'organizer.html')

def participant(request):
    return render(request, 'participant.html')
