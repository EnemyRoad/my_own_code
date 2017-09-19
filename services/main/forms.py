from django import forms
from .models import Data, Payment


class AddData(forms.ModelForm):
    class Meta:
        model = Data
        fields = ('service', 'meters_data', 'month')


class Pay(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ('name', 'count')
