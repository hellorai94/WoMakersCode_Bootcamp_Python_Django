from django import forms
from base.models import Cadastro
# Herda do Django
class CadastroForm(forms.ModelForm):
    # Campo do tipo Texto
    class Meta:
        model = Cadastro
        fields = ['nome', 'email', 'senha']
        widgets = {'senha': forms.PasswordInput()}
   