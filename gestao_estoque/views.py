from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, View, UpdateView, CreateView
from .models import Produto, TipoProduto, MarcaProduto
from django.db.models import Q
from django.urls import reverse_lazy


class HomeView(View):
    def get(self, request):
        return render(
            request,
            'gestao_estoque/home.html'
        )



class ProdutosListView(ListView):
    model = Produto
    template_name = 'gestao_estoque/produtos.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset().order_by('id')
        query = self.request.GET.get('search') 
        if query:
            queryset = queryset.filter(
                Q(id__contains=query) | 
                Q(name__icontains=query) | 
                Q(price__icontains=query) | 
                Q(brand__brand__icontains=query) | 
                Q(type__type__icontains=query)
            )
        return queryset

  
    
class ProdutosCreateView(CreateView):
    model = Produto
    fields = '__all__'
    template_name = 'gestao_estoque/produto_create.html'
    success_url = reverse_lazy('produtos')




class ProdutosUpdateView(UpdateView):
    model = Produto
    fields = '__all__'
    template_name = 'gestao_estoque/produto_update.html'
    success_url = reverse_lazy('produtos')

    
class ProdutosRemoveView(View):
    
    def get(self, request, pk):
        produto = get_object_or_404(Produto, id=pk)
        produto.delete()
        return redirect('produtos')
    






class TiposListView(ListView):
    model = TipoProduto
    template_name = 'gestao_estoque/tipo_produtos.html'

    def get_queryset(self):
        queryset = super().get_queryset().order_by('id')
        query = self.request.GET.get('search') 
        if query:
            queryset = queryset.filter(
                Q(id__contains=query) | 
                Q(type__icontains=query) 
            )
        return queryset
  
    
class TiposCreateView(CreateView):
    model = TipoProduto
    fields = '__all__'
    template_name = 'gestao_estoque/tipo_produto_create.html'
    success_url = reverse_lazy('tipos')


class TiposUpdateView(UpdateView):
    model = TipoProduto
    fields = '__all__'
    template_name = 'gestao_estoque/tipo_produto_update.html'
    success_url = reverse_lazy('tipos')

    
class TiposRemoveView(View):
    
    def get(self, request, pk):
        tipo = get_object_or_404(TipoProduto, id=pk)
        tipo.delete()
        return redirect('tipos')
    






class MarcasListView(ListView):
    model = MarcaProduto
    template_name = 'gestao_estoque/marca_produtos.html'

    def get_queryset(self):
        queryset = super().get_queryset().order_by('id')
        query = self.request.GET.get('search') 
        if query:
            queryset = queryset.filter(
                Q(id__contains=query) | 
                Q(brand__icontains=query)
            )
        return queryset
  
    
class MarcasCreateView(CreateView):
    model = MarcaProduto
    fields = '__all__'
    template_name = 'gestao_estoque/marca_produto_create.html'
    success_url = reverse_lazy('marcas')


class MarcasUpdateView(UpdateView):
    model = MarcaProduto
    fields = '__all__'
    template_name = 'gestao_estoque/marca_produto_update.html'
    success_url = reverse_lazy('marcas')

    
class MarcasRemoveView(View):
    
    def get(self, request, pk):
        marca = get_object_or_404(MarcaProduto, id=pk)
        marca.delete()
        return redirect('marcas')