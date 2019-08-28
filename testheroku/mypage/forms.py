from django import forms
from .models import MyImage


class MyImageForm(forms.ModelForm):
    name = forms.CharField(label='Name', max_length=128)
    image = forms.ImageField()

    class Meta:
        model = MyImage
        fields = ['name', 'image']
