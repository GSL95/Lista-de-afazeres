"""
URL configuration for Primeiro_crud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from main.views import ListaAfazeresView, ListaAfazeresCreate, ListaAfazeresUpdate, ListaAfazeresDelete, ListaAfazeresConcluir
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ListaAfazeresView.as_view(), name="lista_afazeres_lista"),
    path('create', ListaAfazeresCreate.as_view(),name="todo_create"),
    path('update/<int:pk>', ListaAfazeresUpdate.as_view(), name='lista_afazeres_update'),
    path('delete/<int:pk>', ListaAfazeresDelete.as_view(), name="lista_afazeres_delete"),
    path('complete/<int:pk>', ListaAfazeresConcluir.as_view(), name="lista_afazeres_concluir")

]
