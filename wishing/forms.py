from django import forms
from .models import Wishing

class WishingForm(forms.ModelForm):
   class Meta:
       model = Wishing
       fields =['wishingdate', 'wishingmoney', 'wishingmemo']
