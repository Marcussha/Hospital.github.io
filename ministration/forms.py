from django import forms
from ministration.models import Ministration

class MinistrationForm(forms.ModelForm):
    class Meta :
        model = Ministration
        fields = [ 'minisid','name_ministration'] 
        widgets = { 'minisid': forms.TextInput(attrs={ 'class': 'form-control' }), 
                   'name_ministration': forms.TextInput(attrs={ 'class': 'form-control' }), 
            
        }