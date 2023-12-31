from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register_organizer, name='register'),
    # path('register-organizer/', views.register_organizer, name='register_organizer'),
    path('adminpage/', views.admin, name='adminpage'),
    path('organizer/', views.organizer, name='organizer'),
    path('participant/', views.participant, name='participant'),
    path('register-admin/', views.registeradmin, name='registeradmin'),  # Use hyphen for consistency
]
