from django.shortcuts import render, render_to_response, redirect
from django.views import generic
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from models import *
from forms import *
# Create your views here.
def test(request):
    mascota = Mascota.objects.order_by('nombre_de_mascota')
    return render_to_response('base.html',{"lista":mascota})
    
class Home(View):
    def get(self, request):

        if request.user.is_authenticated and request.user.is_active:
            mascota = Mascota.objects.order_by('nombre_de_mascota')
            return render(request, 'base.html',{"lista":mascota})
        else:
            return redirect('Login')
        
    def post(self, request):
        dt = request.POST.get('search')
        mascota = Mascota.objects.get(nombre_de_mascota=dt)
        return render(request,'base.html',{"lista":mascota})
    
def ordenarPorTipoSangre(request):
    mascota = Mascota.objects.order_by('tipo_sangre')
    return render(request, 'base.html',{"lista":mascota})
   
def ordenarNombreDeMascota(request):
    mascota = Mascota.objects.order_by('nombre_de_mascota')
    return render(request, 'base.html',{"lista":mascota})
    
class UserFormView(View):
    form_class = UserForm
    template_name = 'registration.html'
    
    #display a blank form
    def get(self, request):
        form = self.form_class(None)
        if request.user.is_staff:
            return render(request, self.template_name,{'form':form})
        else:
            return render(request, 'base.html',{})
    
    #process form data
    def post(self, request):
        form = self.form_class(request.POST)
        
        if form.is_valid():
            user = form.save(commit=False)
            
            #cleaned (normalizaed) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            
            #returns User objects if credential are correct
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    return redirect('DBDisplay')
        return render(request, self.template_name, {'form':form})
        
class LoginView(View):
    template_name = 'login.html'

    def get(self, request):
        if request.user.is_authenticated and request.user.is_active:
            return redirect('DBDisplay')
        else:
            return render (request, self.template_name, {})


    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                return redirect ('DBDisplay')
            else:
                 return render (request, self.template_name,{})
        return render (request, self.template_name,{})

        
class LogoutView (View):
    def get (self,request):
        user = request.user 
        if user.is_authenticated:
            logout(request)
            return redirect("Login")
        return redirect("Login")
        
class CrearMascota (View):
    pagina = 'crearmascota.html'
    form_class = MascotaForm 
    def get (self,request):
        if not request.user.is_authenticated():
            return redirect('DBDisplay')
        form = self.form_class(None)
        return render (request,self.pagina,{'form':form})
        
    def post (self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('DBDisplay')
        else:
            return redirect('Login')
            
def deleteMascota (request, id):
    mascota = Mascota.objects.get(pk=id)
    mascota.delete()
    return redirect('DBDisplay')
    
class EditarMascota (View):
    form_class = MascotaForm
    template_name = 'crearmascota.html'
    
    def get (self,request,id):
        if not request.user.is_authenticated():
            return redirect ('DBDisplay')
        mascota = Mascota.objects.get(pk=id)
        form=self.form_class(instance=mascota)
        return render (request,self.template_name, {'form':form})
        
    def post (self,request, id):
        form = self.form_class (request.POST)
        
        if form.is_valid():
            mascota = Mascota.objects.get(pk=id)
            form = self.form_class (request.POST, instance=mascota)
            form.save()
            return redirect ('DBDisplay')
