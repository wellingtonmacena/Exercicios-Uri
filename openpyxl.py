from openpyxl import Workbook

arquivo_excel = Workbook()

planilha_em_uso = arquivo_excel.active

planilha_em_uso.title = "Planilha ativa"

letras = [("Nome", "Sobrenome", "Idade", "telefone", "Cidade", "Casado?", "G", "H")]

dados = [("Wellington", "Macena", 21, 1178973, "são Paulo", "no"),
          ("José", "Almeida", 56, 116534, "sales", "no"),
         ("Daniel", "Clock", 34, 116456, "bloco","no"),
         ("Jp", "Silva", 34, 1174537,"nuvem", "yes"),
         ("Danilo", "glovis", 33,1164554, "Jaú", "yes")]

def inserir_dados(header, dados):

    for letra in header:
        planilha_em_uso.append(letra)

    for ocorrencia in dados:
        planilha_em_uso.append(ocorrencia)

inserir_dados(letras,dados)
arquivo_excel.save("Excel2.xlsx")