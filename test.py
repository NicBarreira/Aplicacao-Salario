import PySimpleGUI as sg

layout = [
    [sg.Text('Qual salário atual? $'), sg.InputText(key='salario')],
    [sg.Text('Quantos % de aumento?'), sg.InputText(key='aumento')],
    [sg.Button('Calcular'), sg.Button('Sair')],
    [sg.Text('Aumento:'), sg.InputText(key='resultado')]
]

window = sg.Window('Calculadora de Aumento de Salário', layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == 'Sair':
        break
    elif event == 'Calcular':
        try:
            salario = float(values['salario'])
            aumento = float(values['aumento'])
            novo_salario = salario + (salario * aumento / 100)
            window['resultado'].update(f'O novo salário será de: ${novo_salario:.2f}')
        except ValueError:
            sg.popup_error('Por favor, insira valores válidos para salário e aumento.')

window.close()