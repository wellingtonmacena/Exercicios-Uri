import xlwt
import os

class python_excel_xls:
    arquivo_excel = xlwt.Workbook()
    planilha1 = arquivo_excel.add_sheet("planilha1")


    xlwt.add_palette_colour("azulzinho", 0x21)
    arquivo_excel.set_colour_RGB(0x21, 204, 255, 255)


    estilo_cabecalho = xlwt.easyxf('font: bold off, color black, height 250, name = "Times New Roman";\
                     borders: bottom_color black,\
                                bottom thick;\
                     pattern: pattern solid, fore_color azulzinho;')

    estilo_corpo = xlwt.easyxf('font: bold off, color black, height 220')

    def criar_planilha(self, header, entrada_dados, abrir_arquivo=False, nome_arquivo='padrão'):
        dados_estruturados = []

    #Criar lista de listas de dicionarios
        for ocorrencia in entrada_dados:
            for elemento in range(0, len(header)):
                dados_estruturados.append({header[elemento]: ocorrencia[elemento]})

    # Inserir cabeçalho excel
        for pos_ocorrencia, ocorrencia in enumerate(header):
            self.planilha1.write(0, pos_ocorrencia, ocorrencia, self.estilo_cabecalho,)


    #Inserir dados no excel
        linha = 0
        posicao =0
        coluna =1


        for vetor in range(len(dados_estruturados)):
            self.planilha1.write(coluna, linha, dados_estruturados[vetor][header[posicao]])
            posicao +=1
            linha+=1

            if posicao ==3:
                posicao= 0
                linha = 0
                coluna+=1


        arquivo_salvo = f"{nome_arquivo}.xls"
        self.arquivo_excel.save(arquivo_salvo)

        if (abrir_arquivo == True):
            os.startfile(arquivo_salvo)


        print(dados_estruturados)
obj_excel = python_excel_xls()
obj_excel.criar_planilha(["nome", "bairro", "telefone"], [["wellington", "paraiso", "119954"],
                                                          ["joao", "consolação", "19954545"],
                                                          ["daniel", "santana", "1100323"],
                                                          ], abrir_arquivo=False, nome_arquivo = 'lista_dicionarios')