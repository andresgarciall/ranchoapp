from msilib.schema import ListView
from django.shortcuts import render
from django.views.generic import ListView
from clientes.models import Cliente

# Create your views here.
class IndexView(ListView):
    template_name= 'clientes/index.html'
    context_object_name = 'clientes'

    def get_queryset(self):
        return Cliente.objects.all()