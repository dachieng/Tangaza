from django import forms 
from .models import *
  
class ProductForm(forms.ModelForm): 
  
    class Meta: 
        model = Upload 
        fields = '__all__'