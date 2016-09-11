"""project_colitas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from app import views

app_name = 'app'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.LoginView.as_view()),
    url(r'^home/$', views.Home.as_view(),name='DBDisplay'),
    url(r'^OrdenarPorTipoSangre/$', views.ordenarPorTipoSangre, name="Ordenar Por Tipo Sangre"),
    url(r'^OrderByNombreDeMascota/$', views.ordenarNombreDeMascota, name="OrdenarNombre"),
    url(r'^registration/$', views.UserFormView.as_view()),
    url(r'^login/$', views.LoginView.as_view(), name="Login"),
    url(r'^logout/$', views.LogoutView.as_view()),
    url(r'^add/$', views.CrearMascota.as_view(),name = "Add"), 
    url(r'^edit/(?P<id>\d+)$', views.EditarMascota.as_view(), name="Edit"),
    url(r'^delete/(?P<id>\d+)$', views.deleteMascota, name='Delete'),
]
