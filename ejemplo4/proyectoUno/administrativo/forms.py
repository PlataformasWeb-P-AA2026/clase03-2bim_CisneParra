from django.forms import ModelForm
from administrativo.models import Estudiante, Pais

class PaisForm(ModelForm):
    class Meta:
        model = Pais
        fields = ['nombre', 'capital', 'nro_provincias', 'nro_habitantes']
class EstudianteForm(ModelForm): 
    class Meta:
        model = Estudiante 
        fields = ['nombre', 'apellido', 'cedula'] 




