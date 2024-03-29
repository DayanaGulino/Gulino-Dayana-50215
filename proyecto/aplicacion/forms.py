from django import forms

class CursoForm (forms.Form):
    curso = forms.CharField (max_length = 48, required= True)
    comision = forms.IntegerField(max_value=100)

class UsuarioForm(forms.Form):
    nombre_agencia = forms.CharField(max_length=48)
    contraseña = forms.CharField(max_length=100)

class StaffForm(forms.Form):
    nombre = forms.CharField(max_length=48)
    apellido = forms.CharField(max_length=48)
    email = forms.EmailField()


class RegistroForm(forms.Form):
    nombre_agencia = forms.CharField(max_length=100, required=True)
    contraseña = forms.CharField(widget=forms.PasswordInput, required=True)
    confirmar_contraseña = forms.CharField(widget=forms.PasswordInput, required=True)

    class Meta:
        model = UsuarioForm
        fields= ['nombre_agencia', 'contraseña', 'confirmar_contraseña']

class UserEditForm(forms.Form):
    nombre_agencia = forms.CharField(max_length=100, required=True)
    contraseña = forms.CharField(widget=forms.PasswordInput, required=True)

    class Meta:
        model = UsuarioForm
        fields= ['nombre_agencia', 'contraseña']

    

class LoginForm(forms.Form):
    nombre_agencia = forms.CharField(max_length=100, required=True)
    contraseña = forms.CharField(widget=forms.PasswordInput, required=True)

 
