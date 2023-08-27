from django import forms
from .models import *
class FinalUserForm(forms.ModelForm):
    class Meta:
        model = Final_User
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        num_fields = [
            cleaned_data['seri1'], cleaned_data['seri2'], cleaned_data['num11'],
            cleaned_data['num12'], cleaned_data['num13'], cleaned_data['num14'],
            cleaned_data['num15'], cleaned_data['num16'], cleaned_data['num17'],
            cleaned_data['num18'], cleaned_data['num19'], cleaned_data['num20'],
            cleaned_data['num21'], cleaned_data['num22'], cleaned_data['num23'],
            cleaned_data['num24']
        ]
        cleaned_data['total'] = sum([field for field in num_fields if field is not None])
        return cleaned_data

class Delete_User(forms.Form):
    button = forms.CharField()