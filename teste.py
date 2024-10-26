from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
import datetime

# id, nome_pagador, total, lista_produtos_comprados
def GeneratePDF(id, total, lista_produtos_comprados, caixa, cnpj, rua_numero, cidade_bairro, metodo_pagamento, nome=False, cpf=False):
    width = 14 * cm
    height = 10 * cm
    data_atual = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
    try:
        # nome_pdf = input('Informe o nome do PDF: ')
        nome_pdf = 'recibo'
        pdf = canvas.Canvas(f'{nome_pdf}.pdf', pagesize=(width, height))
        pdf.drawImage('logotipo.png', 17, height - 53, 60, 60)

        # Configuração da fonte e título
        pdf.setFont("Helvetica-Bold", 16)
        titulo = 'RECIBO'
        largura_titulo = pdf.stringWidth(titulo, "Helvetica-Oblique", 17)
        x_titulo = (width - largura_titulo) / 2
        pdf.drawString(x_titulo, height - 20, titulo)



        # Config Id e Preço
        pdf.setFont('Helvetica', 14)
        text_id = f'Num° {id}'
        pdf.drawRightString(width - 20, height - 20, text=text_id)



        pdf.setFont('Helvetica', 10)
        cnpj_text = cnpj
        rua_text = rua_numero
        cidade_text = cidade_bairro
        pdf.drawString(20, height-50, cnpj_text)
        pdf.drawString(20, height-60, rua_text)
        pdf.drawString(20, height-70, cidade_text)

        pdf.line(20, 205, width-20, 205) 


        cnpj_text = cnpj
        metodo_pagamento
        pdf.drawString((width/2) + 10, height-50, caixa)
        pdf.drawString((width/2) + 10, height-60, data_atual)
        pdf.drawString((width/2) + 10, height-70, 'Método de pagamento: ' + metodo_pagamento)

        
        pdf.setFont("Helvetica-Bold", 17)
        preco_text = 'R$ ' + total
        pdf.drawRightString(width - 20, 13, text=preco_text)



        pdf.setFont("Helvetica-Bold", 13)
        descricao = 'Lista de Produtos'
        largura_descricao = pdf.stringWidth(descricao, "Helvetica-Bold", 13)
        x_descricao = (width - largura_descricao) / 2
        pdf.drawString(x_descricao, height - 95, descricao)


        pdf.setFont("Helvetica", 12)
        cont = height-115
        for k, v in lista_produtos_comprados.items():
            pdf.drawString(20, cont, f'{k} - {v['quantidade']}x')
            pdf.drawRightString(width-20, cont, f'R$ {v['preço']}')
            cont -= 14        

            
        if nome and cpf:
            pdf.setFont('Helvetica', 12)

            pdf.drawString(20, 13, text=nome + ',' + ' CPF: '+ cpf)

        
        
        pdf.setTitle(nome_pdf)
        pdf.save()
        print('{}.pdf criado com sucesso!'.format(nome_pdf))
    except Exception as e:
        print('Erro ao gerar {}.pdf: {}'.format(nome_pdf, e))



nome = 'Alan Pereira Cavalcante'
id = 57
total = '276.5'
cpf = '581.659.778-73'
caixa = 'Caixa número 1'

lista_produtos_comprados = {
    'Red Label 1l': {'preço': 120.5, 'quantidade': 2},
    'Gelo de coco': {'preço': 3.50, 'quantidade': 5},
    'Gelo de melancia': {'preço': 4, 'quantidade': 2},
}
cnpj = 'CNPJ: 68.314.830/0001-27'
rua_numero = 'Rua Benedita Aparecida Nogueira, 81'
cidade_bairro = 'Taboão da Serra - Intercap'
metodo_pagamento = 'PIX'

GeneratePDF(id, total, lista_produtos_comprados, caixa, rua_numero, cidade_bairro, cnpj, metodo_pagamento, nome, cpf)

