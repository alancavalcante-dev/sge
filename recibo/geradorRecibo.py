from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
import datetime
import os
import platform  # Para detectar o sistema operacional

def GeneratePDF(id, total, lista_produtos_comprados, caixa, cnpj, rua_numero, cidade_bairro, metodo_pagamento, nome=False, cpf=False):
    width = 14 * cm
    height = 10 * cm
    data_atual = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
    data_nome_arquivo = datetime.datetime.now().strftime("%d-%m-%Y_%H-%M")
    try:
        nome_pdf = 'recibo'
        caminho_pdf = f'../Gallery/{nome_pdf}_{data_nome_arquivo}.pdf'
        pdf = canvas.Canvas(caminho_pdf, pagesize=(width, height))
        
        # Adiciona conteúdo ao PDF
        pdf.drawImage('../Gallery/logotipo.png', 17, height - 53, 60, 60)
        pdf.setFont("Helvetica-Bold", 16)
        titulo = 'RECIBO'
        largura_titulo = pdf.stringWidth(titulo, "Helvetica-Oblique", 17)
        x_titulo = (width - largura_titulo) / 2
        pdf.drawString(x_titulo, height - 20, titulo)
        pdf.setFont('Helvetica', 14)
        pdf.drawRightString(width - 20, height - 20, text=f'Num° {id}')
        pdf.setFont('Helvetica', 10)
        pdf.drawString(20, height - 50, cnpj)
        pdf.drawString(20, height - 60, rua_numero)
        pdf.drawString(20, height - 70, cidade_bairro)
        pdf.line(20, 205, width - 20, 205)
        pdf.drawString((width / 2) + 10, height - 50, caixa)
        pdf.drawString((width / 2) + 10, height - 60, data_atual)
        pdf.drawString((width / 2) + 10, height - 70, 'Método de pagamento: ' + metodo_pagamento)
        pdf.setFont("Helvetica-Bold", 17)
        pdf.drawRightString(width - 20, 13, text='R$ ' + total)
        pdf.setFont("Helvetica-Bold", 13)
        descricao = 'Lista de Produtos'
        largura_descricao = pdf.stringWidth(descricao, "Helvetica-Bold", 13)
        x_descricao = (width - largura_descricao) / 2
        pdf.drawString(x_descricao, height - 95, descricao)

        pdf.setFont("Helvetica", 12)
        cont = height - 115
        for k, v in lista_produtos_comprados.items():
            pdf.drawString(20, cont, f"{k} - {v['quantidade']}x")
            pdf.drawRightString(width - 20, cont, f"R$ {v['preço']}")
            cont -= 14        

        if nome and cpf:
            pdf.setFont('Helvetica', 12)
            pdf.drawString(20, 13, text=f"{nome}, CPF: {cpf}")

        pdf.setTitle(nome_pdf)
        pdf.save()
        print(f'{nome_pdf}.pdf criado com sucesso!')

        # Impressão automática
        sistema = platform.system()
        if sistema == 'Windows':
            os.startfile(caminho_pdf, "print")
        elif sistema == 'Darwin':  # macOS
            os.system(f'lpr "{caminho_pdf}"')
        elif sistema == 'Linux':
            os.system(f'lp "{caminho_pdf}"')
        else:
            print("Sistema operacional não suportado para impressão automática.")

    except Exception as e:
        print(f'Erro ao gerar {nome_pdf}.pdf: {e}')





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

