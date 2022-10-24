from django import forms
from django.db.models import fields

from .models import  Material

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
       # fields ='__all__'
        fields = ['codigo', 'nome','descricao','id_local', 'id_fornecedor','id_marca', 'id_classifica', 'id_processo' ]