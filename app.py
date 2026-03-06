# Importando as funções de operations
from operations import *

# Lista de móveis de teste
moveis = [
    {"nome": "Cama", "preco": 800, "comprado": False},
    {"nome": "Sofá", "preco": 1200, "comprado": False}
]

# Operações para cada opção do menu
while True:
    exibirMenu()
    escolha = int(input('Sua opção: '))
    if escolha == 0:
        break
    elif escolha == 1:
        visualizarLista(moveis)
    elif escolha == 2:
        nome = str(input('Nome do móvel: '))
        preco = float(input('Preço do móvel: R$'))
        moveis = adicionarMovel(moveis,nome,preco)
    elif escolha == 3:
        nome = str(input('Nome do móvel que será removido: '))
        removerMovel(moveis,nome)
    elif escolha == 4:
        salario = float(input('Salário por dia: R$'))
        gerarCronograma(moveis,salario)
    elif escolha == 5:
        salario = float(input('Salário por dia: R$'))
        gerarBoletim(moveis,salario)
    else:
        print('OPÇÃO INVÁLIDA! Tente novamente!!!')

print('FIM DO PROGRAMA!!!')