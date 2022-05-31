from django import forms

class PersonaForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=100)
    apellido = forms.CharField(label="Apellido", max_length=100)
    email = forms.EmailField(label="Email")
    fecha_nacimiento = forms.DateField(label="fecha_nacimiento", input_formats=["%d/%m/%Y"],
    widget=forms.TextInput(attrs={'placeholder': '24/08/1993'}))
    altura = forms.FloatField(widget=forms.NumberInput(attrs={'placeholder': "1.75 m"}))

class BuscarPersonasForm(forms.Form):
    palabra_a_buscar = forms.CharField(label="Buscar")