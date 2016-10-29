from django import forms
from .models import DatosPersonas


class DatosPersonasForm(forms.ModelForm):
    YESNO_CHOICES = ((0, 'Si'), (1, 'No'))
    capacitacion = forms.TypedChoiceField(
        choices=YESNO_CHOICES, widget=forms.RadioSelect, coerce=int
    )
    motivado = forms.TypedChoiceField(
        choices=YESNO_CHOICES, widget=forms.RadioSelect, coerce=int,
        label='se encuentra motivado para seguir realizando otros estudios?'
    )

    class Meta:
        model = DatosPersonas
        fields = '__all__'
