from django.core.files.storage import FileSystemStorage
from django.template.loader import render_to_string
from django.http import HttpResponse
from weasyprint import HTML
from django.views.generic import View



class Recibo(View):
  def get(self, request, *args, **kwargs):
      texto = [
          'Gerando arquivo PDF', 'Evolua seu lado Programador Django',
          'Programação Web com Python e Django'
          ]
      
      html_string = render_to_string(
          'relatorio.html', 
          {'texto': texto}
          )
      
      html = HTML(
          string=html_string
          )
      
      html.write_pdf(
          target='/templates/relatorio.pdf'
          )
      
      fs = FileSystemStorage('/templates')


      with fs.open('relatorio.pdf') as pdf:
          response = HttpResponse(pdf, content_type='application/pdf')
          # Faz o download do arquivo PDF
          # response['Content-Disposition'] = 'attachment: filename="relatorio2.pdf"'
          # Abre o PDF como página HTML:
          response['Content-Disposition'] = 'inline: filename="relatorio.pdf"'
      return response