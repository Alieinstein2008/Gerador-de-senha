#Importação das bibliotecas
import PySimpleGUI as sg
import random as rd
import os

#Definindo o tema da interface gráfica
sg.theme('darkblue18')

#Criação do layout da interface gráfica
layout = [
    [sg.Text("Diretório para salvamento:"),sg.Input(key=("Caminho"),size=(17,1), default_text=('Área de Trabalho'), readonly=(True), disabled_readonly_background_color=('#001c34')),sg.FolderBrowse()],
    [sg.Text('Índice de referência:  '), sg.Input(size = (21,1), key = ("Referenciador"))],
    [sg.Text('Número de caracteres da senha: '), sg.Input(key = ("NumerosCaracteres"), size = (11,1))],
    [sg.Text('Escolha o tipo da senha:\n', size=(19,1)),sg.Combo(('Apenas Números','Apenas Letras','Apenas Símbolos', 'Todos os Anteriores'),readonly = True, key = ("Tipo"), size = (15,1))],
    [sg.Text()],
    [sg.Button('Gerar Senha'),sg.Button('Sair')],
    [sg.Text()]      
]

window = sg.Window("Gerador de Senha", layout)

#Criação de Variaveis 
Numeros = ['0','1','2','3','4','5','6','7','8','9']
Letras = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','ç','z','x','c','v','b','n','m',
          'á','é','í','ó','ú','à','è','ì','ò','ù','ã','õ','â','ê','î','ô','û',
          'Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Ç','Z','X','C','V','B','N','M',
          'Á','É','Í','Ó','Ú','À','È','Ì','Ò','Ù','Ã','Õ','Â','Ê','Î','Ô','Û']
Simbolos = ['!','@','#','$','%','&','*','(',')',',','_','-','+','=','{','}','[',']','^','~','<','>','.',';',':','?','/']
TodosCaracteres = []
TodosCaracteres = Numeros + Letras + Simbolos

Senha = '' 
ArquivoSalvamentoPadrao = ''
ArquivoSalvamentoSenhaAtual = ''

def GeradorSenha(SenhaGerada,events,values):
    if values["Tipo"] == 'Apenas Números' and QuantidadeCaracteres > 0:
        for numbers in range(0,QuantidadeCaracteres):
            indice = rd.randrange(0,len(Numeros))
            SenhaGerada += Numeros[indice]
    elif values["Tipo"] == 'Apenas Letras' and QuantidadeCaracteres > 0:
        for letters in range(0, QuantidadeCaracteres):
            indice = rd.randrange(0,len(Letras))
            SenhaGerada += Letras[indice]
    elif values["Tipo"] == 'Apenas Símbolos' and QuantidadeCaracteres > 0:
        for simbols in range(0,QuantidadeCaracteres):
            indice = rd.randrange(0,len(Simbolos))
            SenhaGerada += Simbolos[indice]
    elif values["Tipo"] == 'Todos os Anteriores' and QuantidadeCaracteres > 0:
        for caracteres in range(0, QuantidadeCaracteres):
            indice = rd.randrange(0,len(TodosCaracteres))
            SenhaGerada += TodosCaracteres[indice]
    return SenhaGerada

while True:
    events,values = window.read()
    if events == ('Gerar Senha') and values["NumerosCaracteres"] != '' and values["Tipo"] != '' :
        QuantidadeCaracteres = int(values["NumerosCaracteres"])
        if values["Caminho"] == 'Área de Trabalho':
            #Utilizando a bibliteca os para salvar por padrão, caso o caminho não seja especificado, o arquivo de senha na área de trabalho
            CaminhoSalvamentoSenhaPadrao = os.path.join(os.environ["USERPROFILE"], "Desktop")
            ArquivoSalvamentoPadrao = open(r"{}\Senhas.txt".format(CaminhoSalvamentoSenhaPadrao),'a') 
            SenhaGerada = GeradorSenha(Senha,events,values)
            if values["Referenciador"] != '':
                ArquivoSalvamentoPadrao.writelines('{}: {}\n'.format(values["Referenciador"],SenhaGerada))
                pass
            else:
                ArquivoSalvamentoPadrao.writelines('Referenciador não especificado: {}\n'.format(SenhaGerada))
                pass
            sg.popup("A senha gerada foi: {}\n\nArmazenada com sucesso no arquivo 'Senhas.txt' na Área de Trabalho!\n".format(SenhaGerada))

        else:
            CaminhoSalvamentoSenhaAtual = str(values["Caminho"])
            ArquivoSalvamentoSenhaAtual = open(r"{}/Senhas.txt".format(CaminhoSalvamentoSenhaAtual),'a')
            SenhaGerada = GeradorSenha(Senha,events,values)
            if values["Referenciador"] != '':
                ArquivoSalvamentoSenhaAtual.writelines('{}: {}\n'.format(values["Referenciador"],SenhaGerada))
                pass
            else:
                ArquivoSalvamentoSenhaAtual.writelines('Referenciador não especificado: {}\n'.format(SenhaGerada))
                pass
            sg.popup("A senha gerada foi: {}\n\nArmazenada com sucesso no arquivo 'Senhas.txt' no seguinte caminho: {}\n".format(SenhaGerada,CaminhoSalvamentoSenhaAtual))
        
    
    #Caso o usuário feche ou clique em sair da tela
    elif events == sg.WINDOW_CLOSED or events == 'Sair':
        if ArquivoSalvamentoSenhaAtual != '':
            ArquivoSalvamentoSenhaAtual.close()
            break
        elif values["Caminho"] == 'Área de Trabalho' and ArquivoSalvamentoPadrao != '' :
            ArquivoSalvamentoPadrao.close()
            break
        else:
            break

    #Caso o usuário não informe nenhum dos dados
    elif values["NumerosCaracteres"] == '' and values["Tipo"] == '' and values["Referenciador"] == '' and values["Caminho"] == '/Desktop':
        sg.popup('Dados passados incorretamente, revise-os e corrija os erros', title=('Error'))

    #Caso o usuário não informe o diretório
    elif values["Caminho"] == '':
        sg.popup('Dados passados incorretamente.\nInsira o diretório para salvamento do arquivo contendo a senha a ser gerada!\n', title=('Error'))
    
    #Caso o usuário não informe a quantidade de caracteres que deseja que a senha tenha
    elif values["NumerosCaracteres"] == '':
        sg.popup('Dados passados incorretamente.\nInsira o número de caracteres da senha a ser gerada!\n', title=('Error'))

    #Caso o usuário não selecione o tipo da senha a sr gerada
    elif values["Tipo"] == '':
        sg.popup('Dados passados incorretamente.\nInsira o tipo de senha a ser gerada!\n', title=('Error'))

    
window.close()

