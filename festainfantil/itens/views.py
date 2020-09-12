from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from temas.models import Tema
from .forms import ItemForm


def adicionar(request, id):
    tema = get_object_or_404(Tema, pk=id)
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.tema = tema
            item.save()
            messages.success(request, 'Item adicionado com sucesso!')
            return redirect('tema_detalhe', id=id)
        else:
            messages.warning(request, 'Um ou mais campos foram preenchidos incorretamente!')
            return render(request, 'itens/adicionar.html', {'form': form, 'tema': tema})
    else:
        form = ItemForm()
        return render(request, 'itens/adicionar.html', {'form': form, 'tema': tema})
