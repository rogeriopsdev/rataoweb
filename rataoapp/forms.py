from django import forms
from django.db.models import fields

from .models import Material, Marca, Local, Empenho, Processo, Fornecedor, Notafiscal, Classificacao


class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        # fields ='__all__'
        fields = ['codigo', 'nome', 'descricao', 'tombamento', 'uni', 'quant', 'estado',
                  'local', 'valor_unitario', 'valor_total', 'foto',
                  'datareceb', 'processo', 'tipoentrada', 'responsavel', 'data_manute', 'id_local', 'id_fornecedor',
                  'id_marca', 'id_classifica', 'id_nota', 'id_processo', 'id_ne']


class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = '__all__'


class LocalForm(forms.ModelForm):
    class Meta:
        model = Local
        fields = '__all__'


class EmpenhoForm(forms.ModelForm):
    class Meta:
        model = Empenho
        fields = '__all__'


class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = '__all__'


class NotaForm(forms.ModelForm):
    class Meta:
        model = Notafiscal
        fields = '__all__'


class ClassificaForm(forms.ModelForm):
    class Meta:
        model = Classificacao
        fields = ['classe','nome']



