from django.shortcuts import render, get_object_or_404, redirect
from rataoapp.models import Material, Local, Marca,Classificacao

from .forms import MaterialForm, LocalForm, MarcaForm, ClassificaForm

# Create your views here.
def home(request):
    return render(request, 'ratao/home.html')


def editar_material(request, item):
    material = get_object_or_404(Material, pk=item)
    formulario = MaterialForm(instance=material)
    if request.method == "POST":
        formulario = MaterialForm(request.POST, request.FILES, instance=material)
        if formulario.is_valid():
            formulario.save()
            return redirect('materiais')
        else:
            return render(request, 'ratao/editar_material.html', {'formulario': formulario, 'material': material})
    else:
        return render(request, 'ratao/editar_material.html', {'formulario': formulario, 'material': material})


def materiais(request):
    m = Material.objects.all().order_by('tombamento')[:50]
    busca = request.GET.get('search')
    if busca:
        m = Material.objects.filter(tombamento__icontains=busca) or Material.objects.filter(local__icontains=busca)
    return render(request, 'ratao/materiais.html', {'m': m})


def novo_material(request):
    formulario = MaterialForm(request.POST)
    if request.method == 'POST':
        formulario = MaterialForm(request.POST, request.FILES)
        if formulario.is_valid():
            obj = formulario.save()
            obj.save()
            formulario = MaterialForm()

    return render(request, 'ratao/novo_material.html', {'formulario': formulario})


from django.shortcuts import render, get_object_or_404, redirect
from rataoapp.models import Material
from .forms import MaterialForm


# Create your views Local.


def editar_local(request, codigo):
    local = get_object_or_404(Local, pk=codigo)
    form = LocalForm(instance=local)
    if request.method == "POST":
        form = LocalForm(request.POST, request.FILES, instance=local)
        if form.is_valid():
            form.save()
            return redirect('locais')
        else:
            return render(request, 'ratao/editar_local.html', {'form': form, 'local': local})
    else:
        return render(request, 'ratao/editar_local.html', {'form': form, 'local': local})


def locais(request):
    locais = Local.objects.all().order_by('codigo')[:50]
    busca = request.GET.get('search')
    if busca:
        locais = Local.objects.filter(setor__icontains=busca)
    return render(request, 'ratao/locais.html', {'locais': locais})


def novo_local(request):
    form = LocalForm(request.POST)
    if request.method == 'POST':
        form = MaterialForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()
            obj.save()
            form = MaterialForm()

    return render(request, 'ratao/novo_local.html', {'form': form})


# Create your views Marca

def editar_marca(request, codigo):
    marca = get_object_or_404(Marca, pk=codigo)
    form = MarcaForm(instance=marca)
    if request.method == "POST":
        form = MarcaForm(request.POST, request.FILES, instance=marca)
        if form.is_valid():
            form.save()
            return redirect('marcas')
        else:
            return render(request, 'ratao/editar_marca.html', {'form': form, 'marca': marca})
    else:
        return render(request, 'ratao/editar_marca.html', {'form': form, 'marca': marca})


def marcas(request):
    marcas = Marca.objects.all().order_by('codigo')[:50]
    busca = request.GET.get('search')
    if busca:
        marcas = Marca.objects.filter(codigo__icontains=busca)or Marca.objects.filter(nome__icontains=busca)
    return render(request, 'ratao/marcas.html', {'marcas': marcas})


def nova_marca(request):
    form = MarcaForm(request.POST)
    if request.method == 'POST':
        form = MarcaForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()
            obj.save()
            form =MarcaForm()

    return render(request, 'ratao/nova_marca.html', {'form': form})


# Create your views Classes

def editar_classe(request, codigo):
    classe = get_object_or_404(Classificacao, pk=codigo)
    form = MarcaForm(instance=classe)
    if request.method == "POST":
        form = ClassificaForm(request.POST, request.FILES, instance=classe)
        if form.is_valid():
            form.save()
            return redirect('classes')
        else:
            return render(request, 'ratao/editar_class.html', {'form': form, 'classe':classe })
    else:
        return render(request, 'ratao/editar_class.html', {'form': form, 'classe': classe})


def classes(request):
    classes = Classificacao.objects.all().order_by('codigo')[:50]
    busca = request.GET.get('search')
    if busca:
        classes = Classificacao.objects.filter(codigo__icontains=busca)or Classificacao.objects.filter(nome__icontains=busca) or Classificacao.objects.filter(classe__icontains=busca)
    return render(request, 'ratao/classes.html', {'classes': classes})


def nova_classe(request):
    form = ClassificaForm(request.POST)
    if request.method == 'POST':
        form = ClassificaForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()
            obj.save()
            form =ClassificaForm()

    return render(request, 'ratao/nova_class.html', {'form': form})




