import requests
import os
import time

MAGENTA = "\033[95m"
RESET = "\033[0m"
NEGRITO = "\033[1m"

def limpar_tela():
    os.system('clear')

def mostrar_figlet():
    print(f'''{MAGENTA}{NEGRITO}__     ___      _             _   _  ___  
\ \   / (_) ___| |_ ___  _ __| | | |( _ ) 
 \ \ / /| |/ __| __/ _ \| '__| |_| |/ _ \ 
  \ V / | | (__| || (_) | |  |  _  | (_) |
   \_/  |_|\___|\__\___/|_|  |_| |_|\___/
   {RESET}''')

limpar_tela()

while True:
    mostrar_figlet()
    cep = input(f'{NEGRITO}Digite um CEP: {RESET}')
    url = f'https://viacep.com.br/ws/{cep}/json'

    requisicao = requests.get(url)

    if requisicao.status_code == 200:
        limpar_tela()
        mostrar_figlet()
        print('')
        resultado = requisicao.json()
        print(f"CIDADE: {resultado.get('localidade')}")
        print(f"ESTADO: {resultado.get('uf')}")
        print(f"DDD: {resultado.get('ddd')}")
    else:
        print(f'Error Status Code= {requisicao.status_code}')
        time.sleep(1)
        limpar_tela()
        continue
    print('')

    continuar = input(f'{NEGRITO}Deseja consultar outro cep? s/n: {RESET}')
    if continuar.lower() == 's':
        limpar_tela()
        continue
    else:
        limpar_tela()
        print('Saindo...')
        time.sleep(1)
        limpar_tela()
        break


# https://github.com/victorh8
