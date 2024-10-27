from django.shortcuts import render
from django.views.generic import View



class CaixaView(View):

    def get(self, request):
        return render(
            request,
            'app/base.html', {
                'produto': {
                    'produto_id': 1,
                    'nome': 'Whisky'
                }
            }
        )