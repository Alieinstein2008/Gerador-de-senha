import PySimpleGUI as sg                
import time
import pyscreenshot as ImageGrab
#Interface
layout = [
            [sg.Text("Printador 2000")],
            [sg.Text('Nome.JPG:'), sg.Input(key="name_f",size=(10,1))],       
            [sg.Button('Print'),sg.Button('Sair')]
]        
#Variaveis
window = sg.Window('P2000', layout)    
n_fotos = 0
#Funcao de print
def Tirar_Print():
    imagem = ImageGrab.grab()    
    imagem.save(fp = "/home/pi/Desktop/Prints",
                format = "{}.jpg".format(n_fotos),
                format = "jpeg") 
#laço de repetição principal    
while True:
    events,values = window.read()
    if events == sg.WINDOW_CLOSED or events == 'Sair':
        break
    if events == 'Print':
        window.hide()
        time.sleep(1)
        n_fotos = values["name_f"]
        Tirar_Print()
        time.sleep(1)
        window.un_hide()
        events,values = ('','')

window.close()        
