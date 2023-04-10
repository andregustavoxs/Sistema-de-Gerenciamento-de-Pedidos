# Armazena o nome do pedido que o cliente escolhe e o total que ele vai pagar... No caso, são 3 mesas.

mesas = {
    1: {"pedido": {}, "total": 0},
    2: {"pedido": {}, "total": 0},
    3: {"pedido": {}, "total": 0}
}

# Tabela de preços dos produtos disponíveis no restaurante...

produtos = {
    "refrigerante": 1.5,
    "hamburguer": 12.0,
    "hot-dog": 9.5
}

# Mostra a data e horas atuais com métodos today() e now()
# Strptime = transforma uma string em um objeto datetime
# %d, %m, %Y = diretivos

def mostrar_hora():
    from datetime import date, time, datetime
    hoje = date.today().strftime('%d/%m/%Y')
    agora = datetime.now().strftime('%d/%m/%Y %H: %M')
    print(f'Dia em que a conta foi fechada: {hoje}')
    print(f"Data e horas atuais da conta: {agora}")

# Nessa parte, o atendente vai estar criando uma comanda. O programa vai pedir qual é o número da mesa que vai ser registrado, lembrando que estão disponíveis a mesa 1, mesa 2 e mesa 3. 
# Se o atendente escreveu o número da mesa errado, ele vai pedir para digitar novamente.

def registrar_pedido():
    mesa = int(input("Digite o número da mesa: "))
    while mesa not in mesas:
        mesa = int(input("Mesa não encontrada. Digite novamente o número da mesa: "))
    
    for item, preco in produtos.items():
        print(f"Produtos: {item} - R${preco}")
    produto = input("Digite o produto que foi pedido (refrigerante, hamburguer ou hot-dog): ")
    
# Para cada produto que não estiver no dicionário "produtos", o programa não vai reconhecer...

    while produto not in produtos:
        produto = input("Produto não encontrado. Digite novamente o produto que foi pedido (refrigerante, hamburguer ou hot-dog): ")
    
    quantidade = int(input("Digite a quantidade do produto que foi pedido: "))
    
# Cria uma chave com o nome do pedido, e a quantidade desse pedido como valor.
# Se o produto não foi pedido antes, adicione. Caso foi adicionado, multiplique a quantidade vezes o valor dele.

    if produto in mesas[mesa]["pedido"]:
        mesas[mesa]["pedido"][produto] += quantidade
    else:
        mesas[mesa]["pedido"][produto] = quantidade
    
# Essas são as informações do atendente fazendo o pedido em tempo real...
# Se a mesa "x" pediu 4 refrigerantes, então...
# Saída: Pedido registrado com sucesso para a mesa 2.
# Saída: 4 refrigerante(s) adicionado(s) à mesa 2.
# Saída: Total atual da mesa 2: R$6.00

    mesas[mesa]["total"] += quantidade * produtos[produto]
    
    print(f"Pedido registrado com sucesso para a mesa {mesa}.")
    print(f"{quantidade} {produto}(s) adicionado(s) à mesa {mesa}.")
    print(f"Total atual da mesa {mesa}: R${mesas[mesa]['total']:.2f}")

# Caso o cliente já queira encerrar a conta...

def fechar_conta():
    mesa = int(input("Digite o número da mesa para fechar a conta: "))
    while mesa not in mesas:
        mesa = int(input("Mesa não encontrada. Digite novamente o número da mesa: "))
    
# Imprime os pedidos totais
# Saída: Pedidos da mesa 2: 4 refrigerantes

    print(f"Pedidos da mesa {mesa}:")
    for produto, quantidade in mesas[mesa]["pedido"].items():
        print(f"{quantidade} {produto}(s)")
    
# Imprime o total da conta da mesa
# Saída: Total da mesa 2: R$ 6,00

    print(f"Total da mesa {mesa}: R${mesas[mesa]['total']:.2f}")
    
# Salva as informações em um arquivo TXT

    with open("comandas.txt", "a") as arquivo:
        arquivo.write(f"Mesa {mesa}:\n")
        for produto, quantidade in mesas[mesa]["pedido"].items():
            arquivo.write(f"{quantidade} {produto}(s)\n")
        arquivo.write(f"Total: R${mesas[mesa]['total']:.2f}\n\n")
    
# Caso a mesa já tenha fechado a conta, o programa vai zerar as informações dela....

    mesas[mesa]["pedido"] = {}
    mesas[mesa]["total"] = 0
    
    print(f"Conta da mesa {mesa} fechada com sucesso.")
    mostrar_hora()

# Programa principal...

while True:
    print("\n--- Gerenciamento de Pedidos ---")
    print("1. Registrar Pedido")
    print("2. Fechar Conta")
    print("3. Encerrar Programa")

    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
        registrar_pedido()
    elif opcao == "2":
        fechar_conta()
    elif opcao == "3":
        break
    else:
        print("Opção inválida. Digite novamente.")
