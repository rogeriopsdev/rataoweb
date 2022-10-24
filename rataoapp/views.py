from django.shortcuts import render
from rataoapp.models import Material
from .forms import MaterialForm


# Create your views here.
def mostrar_materiais(request):
    m = Material.objects.all()
    return render(request, 'ratao/materiais.html',{'m':m})


def novo_material(request):
    formulario = MaterialForm(request.POST)
    if request.method =='POST':
        formulario = MaterialForm(request.POST, request.FILES)
        if formulario.is_valid():
            obj = formulario.save()
            obj.save()
            formulario=MaterialForm()

    return render(request,'ratao/novo_material.html',{'formulario':formulario})
