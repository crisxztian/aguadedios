from django.forms import ModelForm, TextInput, NumberInput, Select, DateInput, EmailInput, CheckboxInput, FileInput,PasswordInput
from aguadedios.models import empresas, administradores, barrios
from django import forms

class empresasForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(empresasForm, self).__init__(*args, **kwargs)
        nombres = [(pt.id, pt.nombre) for pt in barrios.objects.all()]
        self.fields['barrio'].choices = nombres
        for field in self.fields.values():
            field.error_messages = {'required':'El campo {fieldname} es obligatorio'.format(
                fieldname=field.label)}

    class Meta:
        model = empresas
        fields = ['barrio','fechacenso', 'nombre', 'identificacion', 'direccion', 'propietario', 'email', 'telefono', 'fecharegistro',
        'actividad', 'regimen', 'naturaleza',  'stiker', 'ica', 'observaciones', 'fotos']
        widgets = {
            'barrio': Select(attrs={'class':'form-control'}),
            'fechacenso': DateInput(attrs={'class':'form-control','type': 'date'}),
            'nombre': TextInput(attrs={'class':'form-control'}),
            'identificacion': TextInput(attrs={'class':'form-control'}),
            'direccion': TextInput(attrs={'class':'form-control'}),
            'propietario': TextInput(attrs={'class':'form-control'}),
            'email': EmailInput(attrs={'class':'form-control'}),
            'telefono': NumberInput(attrs={'class':'form-control'}),
            'fecharegistro': DateInput(attrs={'class':'form-control','type': 'date'}),
            'actividad': Select(attrs={'class':'form-control'}),
            'regimen': Select(attrs={'class':'form-control'}),
            'naturaleza': Select(attrs={'class':'form-control'}),
            'stiker': NumberInput(attrs={'class':'form-control'}),
            'ica': CheckboxInput(attrs={'class':'form-control'}),
            'observaciones': TextInput(attrs={'class':'form-control'}),
            'fotos': FileInput(attrs={'class':'form-control'}),
        }
        labels={
            'barrio': 'Barrio',
            'fechacenso':'Fecha del censo',
            'nombre':'Nombre comercial',
            'identificacion':'C.C. o NIT',
            'direccion':'Dirección',
            'propietario':'Propietario',
            'email':'Correo electrónico',
            'telefono':'Teléfono',
            'fecharegistro':'Fecha de registro',
            'actividad':'Actividad económica',
            'regimen':'Regimen Tributario',
            'naturaleza':'Naturaleza juridica',
            'stiker':'Stiker #',
            'ica':'Inscrito ICA',
            'observaciones':'Observaciones',
            'fotos':'Imagen del lugar',
        }

class empresasUpdateForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(empresasUpdateForm, self).__init__(*args, **kwargs)
        nombres = [(pt.id, pt.nombre) for pt in barrios.objects.all()]
        self.fields['barrio'].choices = nombres

    class Meta:
        model = empresas
        fields = ['barrio','direccion', 'email', 'telefono', 'ica', 'observaciones', 'fotos']
        widgets = {
            'barrio': Select(attrs={'class':'form-control'}),
            'direccion': TextInput(attrs={'class':'form-control'}),
            'email': EmailInput(attrs={'class':'form-control'}),
            'telefono': NumberInput(attrs={'class':'form-control'}),
            'ica': CheckboxInput(attrs={'class':'form-control'}),
            'observaciones': TextInput(attrs={'class':'form-control'}),
            'fotos': FileInput(attrs={'class':'form-control'}),
        }
        labels={
            'barrio': 'Barrio',
            'direccion':'Dirección',
            'email':'Correo electrónico',
            'telefono':'Teléfono',
            'ica':'Inscrito ICA',
            'observaciones':'Observaciones',
            'fotos':'Imagen del lugar',
        }

class administradoresForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(administradoresForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.error_messages = {'required':'El campo {fieldname} es obligatorio'.format(
                fieldname=field.label)}

    class Meta:
        model = administradores
        fields = ['usuario', 'clave']
        widgets = {
            'usuario': TextInput(attrs={'class':'form-control'}),
            'clave': PasswordInput(attrs={'class':'form-control'}),
        }
        labels={
        'usuario': 'Usuario',
        'clave': 'Clave',
        }

class loginForm(forms.Form):
    usuario = forms.CharField(widget=TextInput(attrs={'class':'form-control'}))
    contraseña = forms.CharField(widget=PasswordInput(attrs={'class':'form-control'}))

class barriosForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(barriosForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.error_messages = {'required':'El campo {fieldname} es obligatorio'.format(
                fieldname=field.label)}

    class Meta:
        model = barrios
        fields = ['nombre']
        widgets = {
            'nombre': TextInput(attrs={'class':'form-control'}),
        }
        labels={
        'nombre': 'Nombre',
        }
