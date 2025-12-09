from django.contrib import admin
from django.urls import path, include
from .views import dashboard, login_view, historico, logout_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('dashboard/historico/', historico, name='historico')
]
