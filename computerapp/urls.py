from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('index.html',views.index, name='index'),
    path('login.html',views.login, name='login'),
    path('machines.html',views.machine_list, name='machines'),
    path('utilisateurs.html',views.utilisateurs, name='utilisateurs'),

]
