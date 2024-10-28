from django.shortcuts import render
from django.views.generic import View
from django.db.models import Q
from gestao_estoque.models import Produto


class CaixaView(View):

    def get(self, request):
        produtos = Produto.objects.all()
        search = request.GET.get('search')
        
        if search:
            produtos = produtos.filter(
                Q(id__contains=search) |
                Q(name__icontains=search) |
                Q(brand__brand__icontains=search) |
                Q(type__type__icontains=search)
            )

        return render(
            request,
            'caixa/caixa.html', {
                'produtos': produtos
            }
        )
