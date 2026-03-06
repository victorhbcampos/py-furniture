def exibirMenu():
    """
    -> Função que exibe as opções do menu
    """
    print('-'*30)
    print('Escolha uma opção:')
    print('1 - Visualizar Móveis\n2 - Adicionar um móvel\n3 - Remover um móvel\n4 - Cronograma\n5 - Boletim\n0 - Sair')
    print('-'*30)

def visualizarLista(lista=''):
    """
    -> Função que mostra o nome e o preço dos móveis presentes na lista
    :param lista: Lista de móveis
    """
    print('-'*30)
    print('LISTA DE MÓVEIS')
    print('-'*30)
    for item in lista:
        print(f'{item["nome"]} - R${item["preco"]:.2f}')
    print('-'*30)

def adicionarMovel(lista='',nome='',preco=0):
    """
    -> Função que adiciona um móvel (item) à lista de móveis
    :param lista: Lista de movéis
    :param nome: Nome do móvel
    :param preco: Preço do móvel
    :return: Lista com o novo móvel adicionado
    """
    movel = {"nome": nome, "preco": preco, "comprado": False}
    lista.append(movel.copy())
    print(f'{movel["nome"]} com valor de R${movel["preco"]:.2f} foi adicionado com sucesso à lista!')
    return lista

def removerMovel(lista='',nome=''):
    """
    -> Função que remove um móvel (item) da lista de móveis
    :param lista: Lista de movéis
    :param nome: Nome do móvel
    :return: Lista com o móvel removido.
    """
    try:
        nomes = [m["nome"] for m in lista]
        indice = nomes.index(nome)
        lista.pop(indice)
        print(f"{nome} foi removido da lista!")
    except ValueError:
        print(f"{nome} não foi encontrado na lista!")
    
    return lista

def gerarCronograma(lista='', salario=0):
    """
    -> Função que gera um cronograma de compra dos móveis
    :param lista: Lista de movéis
    :param salario: Salário diário
    """
    # Ordenando do menor para o maior preço
    lista.sort(key=lambda item: item["preco"])
    saldo = dias = 0
    for item in lista:
        while True:
            saldo += salario
            dias += 1
            if saldo >= item['preco']:
                print(f'{item['nome']} no valor de R${item['preco']} foi comprado no dia {dias}.')
                saldo -= item['preco']
                item['comprado'] = True
                break

def gerarBoletim(lista='',salario=0):
    """
    -> Função que gera um boletim com os dias necessários para comprar um determinado móvel
    :param lista: Lista de móveis
    :param salario: Salário diário
    """
    # Ordenando do menor para o maior preço
    lista.sort(key=lambda item: item["preco"])
    for item in lista:
        saldo = dias = 0
        while True:
            saldo += salario
            dias += 1
            if saldo >= item['preco']:
                print(f'São necessários {dias} dias para comprar {item['nome']} no valor de R${item['preco']}.')
                item['comprado'] = True
                break