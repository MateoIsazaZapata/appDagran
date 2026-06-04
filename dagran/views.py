from django.shortcuts import render, redirect 
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, request
from .models import Alerta, Nivel_alerta, Reporte
from .forms import ReporteForm, LoginForm
from django.contrib import messages
import os
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string

# Create your views here.

def login_view(request):
    form = LoginForm(request.POST or None)
    error_message = None
    if form.is_valid():
        nombre = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        user = authenticate(request, username=nombre, password=password)
        
        if user:
            login(request, user)
            messages.success(request, f"Inicio de sesion exitoso")
            return redirect("dashboard")
        else:
            messages.error(request, "Usuario o constraseña incorrecta")
            
    return render(request, "login.html", {'form': form, 'error_message':error_message})


@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "Cierre de sesion exitoso")
    return redirect('login')


@login_required
def dashboard(request):
    nivelAlerta = Nivel_alerta.objects.all()
    alertas = Alerta.objects.all()
    form = ReporteForm(request.POST or None)

    if form.is_valid():
        # Guardar y capturar el objeto Reporte
        reporte = form.save()
        user = request.user
        messages.success(request, "Reporte enviado con éxito")

        # Construir contexto para la plantilla HTML
        estructura = {
            'fecha': reporte.fecha,
            'alerta': reporte.Alerta,  # si es FK, puedes usar reporte.alerta.nombre
            'nivel_alerta': reporte.nivel_alerta,
            'user': request.user,
            'descripcion': reporte.descripcion,
        }

        # Renderizar plantilla HTML
        html_content = render_to_string('plantilla.html', estructura)

        # Construir correo
        email = EmailMultiAlternatives(
            subject='🚨 NUEVA ALERTA RIESGO DE DESASTRE NATURAL 🚨',
            body='Este correo requiere un cliente compatible con HTML.',
            from_email=os.environ.get('EMAIL_HOST_USER'),
            to=[os.environ.get('SMTP_EMAIL_TO_SEND')]
        )
        email.attach_alternative(html_content, 'text/html')
        

        # Enviar correo
        try:
            email.send()
            messages.success(request, 'Correo electrónico enviado con éxito')
        except Exception as e:
            print(f'Error al enviar correo: {e}')
            messages.error(request, "Error en el envío del correo electrónico")

        return redirect('dashboard')

    return render(request, "dashboard.html", {
        'form': form,
        'alertas': alertas,
        'nivelAlerta': nivelAlerta
    })

@login_required
def historico(request):
    reportes = Reporte.objects.all()
    return render(request, "historico.html", {'reportes': reportes})