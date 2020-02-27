from openpyxl import Workbook
import xlwt

def extensao_xls():
    arquivo_excel = xlwt.Workbook()
    planilha1 = arquivo_excel.add_sheet("Planilha1")

    header = ["Nome", "Idade", "Sexo","País", "Profissão","Hobby", "Telefone"]
    dados = [
        ["Carlos", "21", "M", "Brasil"],
        ["João", "32", "M", "Brasil"],
        ["Marcos","12", "M", "Brasil","","Ler"],
        ["Paula", "19","F", "Irã"],
        ["Carmem","46","F", "Argentina"]
    ]
    contadorVertical = 1
    contadorHorizontal = 0

    for elemento in header:
        planilha1.write(0,contadorHorizontal, elemento)
        contadorHorizontal +=1

    for ocorrencia in dados:
        indice_dado = 0
        for dado in ocorrencia:
            planilha1.write(contadorVertical, indice_dado, dado)
            indice_dado +=1
        contadorVertical +=1

    arquivo_excel.save("Arquivo.xls")


def extensao_xlsx():
    arquivo_excel = Workbook()

    planilha1 = arquivo_excel.active
    planilha1.title = "Planilha1"

    header = [("Nome", "Idade", "Sexo", "País", "Profissão", "Hobby", "Telefone")]

    dados = [
        ["Carlos", "21", "M", "Brasil","","",11940547612],
        ["João", "32", "M", "Brasil","Professor"],
        ["Marcos","12", "M", "Brasil","","Ler"],
        ["Paula", "19","F", "Irã","Médica"],
        ["Carmem","46","F", "Argentina","","Escalar"]
        ]

    for elemento in header:
        planilha1.append(elemento)

    for elemento in dados:
        planilha1.append(elemento)

    arquivo_excel.save("Arquivo.xlsx")

extensao = input("Qual a extensão de arquivo desejada: XLS(1) ou XLSX(2): ")

if extensao == "1":
    extensao_xls()
else:
    extensao_xlsx()