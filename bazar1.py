print("BAZAR CIBE AD CAMORIM")
print("Controle de estoque e Orçamentário")
print()

ITENS = ( 
              'vestido rosa', 'vestido preto', 'vestido bege', 'vestido cinza',
              'blusa branca', 'blusa estapada', 'blusa terracota', 'blusa colorida',
              'moletom1', 'moletom2', 'moletom3', 'moletom4',
              'sapato1', 'tênis2', 'sapato3', 'tênis4'
               )
print(ITENS)
print()

#Protótipos de itens do bazar para rodar programa

estoque = [
            'vestido rosa', 'vestido preto', 'vestido bege', 'vestido cinza',
            'blusa branca', 'blusa estapada', 'blusa terracota', 'blusa colorida',
            'moletom1', 'moletom2', 'moletom3', 'moletom4',
            'sapato1', 'tênis2', 'sapato3', 'tênis4'
          ]

estoque = [{"item": item, "quantidade": 10} for item in ITENS ]
print(estoque)
    


# Função para registro de vendas e atualização de estoque

def registrar_compra(nome_item, quantidade_vendida):
    for produto in estoque:
        if produto["item"] == nome_item:
            if produto ["quantidade"] >= quantidade_vendida:
              produto["quantidade"] -= quantidade_vendida
              print(f'{quantidade_vendida} unidade de {nome_item} vendidadas.')
            else: 
               print(f'Estoque insuficiente para {nome_item}. Quantidade disponível: {produto["quantidade"]}')
            break
        else:
            print('Item não encontrado em Estoque')
print()
print()

#campus do usuário, validação de compra, mais tratamento de possíveis comandos não permitidos para funcções inexistentes no programa afim de que ele nao quebre

while True:
    nome_item = input('Digite o item desejado ou "SAIR" para encerrar: ')
    if nome_item.lower() == "sair":
        print()
        print('VOCÊ FINALIZOU COMPRA!')
        break
    try:
        quantidade_vendida = int(input('Digite a quantidade vendida de Item: '))
        registrar_compra(nome_item, quantidade_vendida)
        print('Estoque Final/atualizado:', estoque)
    except:
        print('Por favor, digite um número válido para a quantidade!')


