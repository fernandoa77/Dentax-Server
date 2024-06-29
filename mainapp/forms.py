from django import forms
from .models import RegistroPacienteCdb, DoctorCdb
import uuid


class RegistroPacienteForm(forms.ModelForm):
    class Meta:
        model = RegistroPacienteCdb
        fields = '__all__'

    def save(self, commit=True):
        instance = super().save(commit=False)
        if not instance.id:
            instance.id = f'C{uuid.uuid4()}'
        if commit:
            instance.save()
        return instance


class DoctorForm(forms.ModelForm):
    class Meta:
        model = DoctorCdb
        fields = '__all__'

    def save(self, commit=True):
        instance = super().save(commit=False)
        if not instance.id:
            instance.id = f'C{uuid.uuid4()}'
        if commit:
            instance.save()
        return instance
