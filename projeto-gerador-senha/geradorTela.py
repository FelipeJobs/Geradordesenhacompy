import PySimpleGUI as sg
import random, string
import os
import playsound
sg.theme('Darkblack')# eu usei esse comando para coloca o tema de fundo
playsound.playsound('xxxxxx.mp3',block=False)
layout = [ # aqui eu criei os botões da minha tela.
    [sg.Image('imagem1.png', pad=(0, (20, 10)))],
    [sg.Text('Tamanho da senha (Dígitos): ', font='Heveltica, 20'),
     sg.Input(size=(5,2), font='Heveltica, 20', key='tamanho')],
    [sg.Text('Usuário', font='Heveltica, 20', pad=(0, (20, 20)))],
    [sg.Input(font='Heveltica 20', key='simbol', size=(100, 15), pad=(0, (0, 10)))],
    [sg.Text('Senha', font='Heveltica 20', pad=(0, (15,15)))],
    [sg.InputText(size=(32,5), font='Arial, 28', pad=(0, (5,5)), key='saida')],
    [sg.Button('GERAR', size=(8, 1), font='Arial 12', pad= (0, (10,10))), sg.Button('Sair', size=(8, 1), font='Arial 12',pad= (0, (10,10)))]
]
tela = sg.Window('Gerador de senha', element_justification='center', layout=layout,
                 size=(700, 450), finalize=True)
while True:
    event, values = tela.read()
    if event == sg.WIN_CLOSED: # esse comando é para caso o usuário aperte no X a tele feche
        break

    if event == 'GERAR' and values['tamanho'] == '':
        sg.popup('Informe o tamanho da senha!')
        continue
        # todos esse comando abaixo servem para gerar a senha do usuário.
    elif event == 'GERAR':
        senha = ''
        valores = string.ascii_letters
        valores += string.digits
        valores += string.punctuation
        for c in range(int(values['tamanho'])):
            senha += random.choice(valores)
        # esse comando de baixo gera o resultado no campo criado abaixo de senha.
        tela['saida'].update(senha)

    elif event == 'Sair':
        break

