from django.shortcuts import render, render_to_response, HttpResponseRedirect, get_object_or_404
from aguadedios.models import empresas,administradores,barrios
from aguadedios.Forms import empresasForm, loginForm, administradoresForm, empresasUpdateForm, barriosForm
from django.contrib import messages
from django import forms
from django.views.decorators.csrf import csrf_exempt

autenticacion = False
usuario = None

def add_admin(request):
    if(autenticacion == False):
        messages.add_message(request, messages.ERROR, "Primero inicia sesión")
        return HttpResponseRedirect("/login")
    form = administradoresForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "El administrador ha sido agregado!")
    return render(request, 'Form_admin.html', {'form': form, 'user' : usuario, "messages": messages.get_messages(request)})

def add_barrio(request):
    if(autenticacion == False):
        messages.add_message(request, messages.ERROR, "Primero inicia sesión")
        return HttpResponseRedirect("/login")
    form = barriosForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            guardado = form.save()
            messages.add_message(request, messages.SUCCESS, "El barrio "+guardado.nombre+" ha sido agregado!")
    return render(request, 'Form_barrio.html', {'form': form, 'user' : usuario, "messages": messages.get_messages(request)})

def list_empresas(request):
    print(autenticacion)
    if autenticacion == True:
        print("true")
        return render_to_response("empresas.html", {"empresas": empresas.objects.all(), "messages": messages.get_messages(request), "barri": barrios.objects.all(), 'user' : usuario})
    else:
        print("false")
        return render_to_response("empresas.html", {"empresas": empresas.objects.all(), "messages": messages.get_messages(request), "barri": barrios.objects.all()})

def add_empresa(request):
    if(autenticacion == False):
        messages.add_message(request, messages.ERROR, "Primero inicia sesión")
        return HttpResponseRedirect("/login")
    form = empresasForm(request.POST or None, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "La empresa ha sido agregada!")
            return HttpResponseRedirect("/empresas/list/")
    return render(request, 'Form_empresas.html', {'form': form, 'user' : usuario})

def update_empresa(request, empresaid):
    if(autenticacion == False):
        messages.add_message(request, messages.ERROR, "Primero inicia sesión")
        return HttpResponseRedirect("/login")
    instance = get_object_or_404(empresas, id=empresaid)
    form = empresasUpdateForm(request.POST or None, request.FILES or None , instance=instance)
    form.fields["barrio"].queryset = barrios.objects.all()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "La empresa ha sido actualizada!")
            return HttpResponseRedirect("/empresas/list/")
    return render(request, 'Form_empresas.html', {'form': form, 'user' : usuario, 'estado': 1} )

def login(request):
    form_class = loginForm
    form = form_class(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            try:
                user = request.POST['usuario']
                query = administradores.objects.get(usuario=user)
                if query.clave == request.POST['contraseña']:
                    global autenticacion
                    autenticacion=True
                    global usuario
                    usuario = user
                    print(usuario)
                    return HttpResponseRedirect("/empresas/list/")
                else:
                    messages.add_message(request, messages.ERROR, "Contraseña incorrecta")
            except empleados.DoesNotExist:
                    messages.add_message(request, messages.ERROR, "El usuario ingresado no existe")
    return render(request, 'login.html', {'form': form, "messages": messages.get_messages(request)})

def logout(request):
    messages.add_message(request, messages.SUCCESS, "Ha cerrado la sesión satisfactoriamente")
    global autenticacion
    autenticacion = False
    return render(request, 'logout.html', {"messages": messages.get_messages(request)})

def filtrar(request, barid):
    bario = barrios.objects.get(pk = barid)
    print(bario.nombre)
    filtradas = empresas.objects.filter(barrio = bario)
    if autenticacion == True:
        return render_to_response("empresas.html", {"empresas": filtradas, "messages": messages.get_messages(request), "barri": barrios.objects.all(), 'user' : usuario, 'pri': bario.nombre})
    else:
        return render_to_response("empresas.html", {"empresas": filtradas, "messages": messages.get_messages(request), "barri": barrios.objects.all(), 'pri': bario.nombre})

@csrf_exempt
def buscar(request):
    if request.method == 'POST':
        info=request.POST['busqueda']
        buscadas = empresas.objects.filter(nombre__icontains=info)
        messages.add_message(request, messages.INFO, "Resultados de busqueda para: "+info )
        if autenticacion == True:
            return render_to_response("empresas.html", {"empresas": buscadas, "messages": messages.get_messages(request), "barri": barrios.objects.all(), 'user' : usuario})
        else:
            return render_to_response("empresas.html", {"empresas": buscadas, "messages": messages.get_messages(request), "barri": barrios.objects.all()})
    return HttpResponseRedirect("/empresas/list/")
