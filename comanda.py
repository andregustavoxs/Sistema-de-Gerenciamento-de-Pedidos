# Armazena o nome do pedido que o cliente escolhe e o total que ele vai pagar... No caso, são 3 mesas.

mesas = {
    1: {"pedido": {}, "total": 0, "pessoas": 0},
    2: {"pedido": {}, "total": 0, "pessoas": 0},
    3: {"pedido": {}, "total": 0, "pessoas": 0}
}

faturamento_total = 0

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
    from datetime import datetime
    hora_atual = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    print(f'Dia e hora em que a conta foi fechada: {hora_atual}')

# Nessa parte, o atendente vai estar criando uma comanda. O programa vai pedir qual é o número da mesa que vai ser registrado, lembrando que estão disponíveis a mesa 1, mesa 2 e mesa 3. 
# Se o atendente escreveu o número da mesa errado, ele vai pedir para digitar novamente.

def registrar_pedido():
    mesa = int(input("Digite o número da mesa: "))
    while mesa not in mesas:
        mesa = int(input("Mesa não encontrada. Digite novamente o número da mesa: "))
    
    print("Produtos - Preços")
    for item, preco in produtos.items():
        print(f"{item} - R${preco}")
    produto = input("Digite o produto que foi pedido (refrigerante, hamburguer ou hot-dog): ").lower()

    # not mesas[mesa]["pedido"] = not mesas[mesa]["pedido"] == {}
    if not mesas[mesa]["pedido"]:
        pessoas = input("Digite a quantidade de pessoas na mesa: ")
        while not pessoas.isnumeric() or int(pessoas) <= 0:
            pessoas = input("Valor inválido! Digite novamente a quantidade de pessoas na mesa: ")
        mesas[mesa]["pessoas"] = int(pessoas)
    
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
    # Global = A variável faturamento_total pode ser acessada e modificada tanto dentro quanto fora da função fechar_conta()
    global faturamento_total
    mesa = int(input("Digite o número da mesa para fechar a conta: "))
    while mesa not in mesas:
        mesa = int(input("Mesa não encontrada. Digite novamente o número da mesa: "))

    faturamento_total = mesas[mesa]["total"]

    # Calcula a divisão da conta por pessoa
    valor_unitario = faturamento_total / mesas[mesa]["pessoas"]
    
# Imprime os pedidos totais
# Saída: Pedidos da mesa 2: 4 refrigerantes

    print(f"Pedidos da mesa {mesa}:")
    for produto, quantidade in mesas[mesa]["pedido"].items():
        print(f"{quantidade} {produto}(s)")
    
# Imprime o total da conta da mesa
# Saída: Total da mesa 2: R$ 6,00

    print(f"Total da mesa {mesa}: R${mesas[mesa]['total']:.2f}")

# Imprime o valor dividido por pessoa

    print(f"O valor dividido por pessoa é: R${valor_unitario:.2f}")
    
# Salva as informações em um arquivo TXT


    with open("comandas.txt", "a") as arquivo:
        arquivo.write(f"Mesa {mesa}:\n")
        for produto, quantidade in mesas[mesa]["pedido"].items():
            arquivo.write(f"{quantidade} {produto}(s)\n")
        arquivo.write(f"Total: R${mesas[mesa]['total']:.2f}\n\n")
        arquivo.write(f"Total por pessoa: R${valor_unitario:.2f}")
    
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
    print("3. Mostrar Faturamento Total")
    print("4. Encerrar Programa")

    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
        registrar_pedido()
    elif opcao == "2":
        fechar_conta()
    elif opcao == "3":
        print("=" * 20)
        print(f"Faturamento total: R${faturamento_total:.2f}")
        print("=" * 20)
    elif opcao == "4":
        break
    else:
        print("Opção inválida. Digite novamente.")
