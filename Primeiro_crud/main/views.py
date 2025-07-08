from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect

from .models import Tarefas

class ListaAfazeresView(ListView):
    model = Tarefas


class ListaAfazeresCreate(CreateView):
    model = Tarefas
    fields = ["title","deadline"]
    success_url = reverse_lazy("lista_afazeres_lista")


class ListaAfazeresUpdate(UpdateView):
    model = Tarefas
    fields = ["title", "deadline"]
    success_url = reverse_lazy("lista_afazeres_lista")

class ListaAfazeresDelete(DeleteView):
    model = Tarefas
    success_url = reverse_lazy("lista_afazeres_lista")

class ListaAfazeresConcluir(View):
    def get(self,request, pk):
        tarefa = get_object_or_404(Tarefas,pk=pk)
        tarefa.mark_has_complete()
        return redirect('lista_afazeres_lista')