from django import forms
from datetime import datetime
from .models import Contacto
from .models import Reserva
from .models import Hotel
class ContactForm(forms.ModelForm):

    class Meta:
        model= Contacto
        fields=["nombre","apellido", "telefono", "correo","direccion","comentario"]


class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'
    
class ReservaForm(forms.ModelForm):
    
    class Meta:
        model= Reserva
        fields=["nombre","apellido","rut","correo","telefono","fecha_entrada","fecha_salida","Habitacion_reservada" ]

        widgets = {
            
            'fecha_entrada': DateTimeInput(attrs={'class': 'form-control'}),
            'fecha_salida': DateTimeInput(attrs={'class': 'form-control'}),
            'Habitacion_reservada': forms.Select(attrs={'class': 'form-control'}),
        }
