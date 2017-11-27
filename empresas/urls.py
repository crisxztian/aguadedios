"""empresas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf import settings
from django.contrib import admin
from aguadedios import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^empresas/list', views.list_empresas, name='list_empresas'),
    url(r'^empresas/add', views.add_empresa, name='add_empresa'),
    url(r'^empresas/update/(?P<empresaid>\d+)', views.update_empresa, name='update_empresa'),
    url(r'^administracion/add', views.add_admin, name='add_admin'),
    url(r'^barrios/add', views.add_barrio, name='add_barrio'),
    url(r'^login', views.login, name='login'),
    url(r'^logout', views.logout, name='logout'),
    url(r'^empresas/filter/(?P<barid>\d+)', views.filtrar, name='filtrar'),
    url(r'^empresas/search', views.buscar, name='buscar'),
]
