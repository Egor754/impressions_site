from django.forms import ModelForm, TextInput, HiddenInput

from myapp.models import Memories


class CreateMemoryForm(ModelForm):
    class Meta:
        model = Memories
        fields = ['title', 'latitude', 'longitude', 'description']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
            }),
            'latitude': HiddenInput(),
            'longitude': HiddenInput(),
            'description': TextInput(attrs={
                'class': 'form-control w-100',
            }),
        }
