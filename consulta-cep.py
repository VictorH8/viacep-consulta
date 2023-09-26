import requests
import os
import time

RESET = "\033[0m"
NEGRITO = "\033[1m"

def limpar_tela():
    os.system('clear')


while True:
    limpar_tela()
    cep = input(f'{NEGRITO}Digite um CEP: {RESET}')
    url = f'https://viacep.com.br/ws/{cep}/json'

    requisicao = requests.get(url)

    if requisicao.status_code == 200:
        limpar_tela()
        print('')
        resultado = requisicao.json()
        print(f"{NEGRITO}CIDADE:{RESET} {resultado.get('localidade')}")
        print(f"{NEGRITO}ESTADO:{RESET} {resultado.get('uf')}")
        print(f"{NEGRITO}DDD:{RESET} {resultado.get('ddd')}")
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
