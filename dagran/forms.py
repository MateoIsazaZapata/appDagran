from .models import Alerta, Nivel_alerta, Reporte
from django import forms
from datetime import date

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Usuario'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'})
    )


class ReporteForm(forms.ModelForm):
    class Meta:
        model = Reporte
        fields = ['Alerta', 'nivel_alerta', 'descripcion', 'fecha']
        widgets = {
            'Alerta': forms.RadioSelect(attrs={
                'class': 'form-check-input me-2 text-institucional fs-5',
                'placeholder': 'Seleccione una alerta',
                'label': 'Seleccione una alerta'
            }),
            
            'nivel_alerta': forms.RadioSelect(attrs={
                'class': 'form-check-input d-flex flex-row me-2 text-institucional fw-bold fs-4',
                'placeholder': 'Seleccione un nivel de alerta ',
                'label': 'Seleccione un nivel de alerta'
            }),
            
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control text-institucional mb-4 text-center fs-6 fw-bold',
                'placeholder': 'Describa la alerta'
            }),
            
            'fecha': forms.DateInput(attrs={
                'class': 'form-control text-amarillo mb-4 text-center fs-5 fw-bold',
                'type': 'date',
                'value': date.today().strftime('%Y-%m-%d'),
                'readonly': 'readonly'
            })
        }