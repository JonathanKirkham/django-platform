from django.forms import ModelForm
from .models import Room


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        verbose_name = 'ModelName'
        verbose_name_plural = 'ModelNames'
