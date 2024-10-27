from django.views.generic import View
from django.shortcuts import render



class Recibo(View):

    def get(self, request):
        return render(
            request,
            'gestao_estoque/home.html'
        )

    def post(self, request):
        ...