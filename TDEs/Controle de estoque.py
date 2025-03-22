# Dicionário para armazenar os produtos (nome -> quantidade)
estoque = {}

def adicionar_produto(nome, quantidade):
    if nome in estoque:
        estoque[nome] += quantidade
    else:
        estoque[nome] = quantidade
    print(f"{quantidade} unidades de {nome} adicionadas ao estoque.")

def remover_produto(nome):
    if nome in estoque:
        del estoque[nome]
        print(f"{nome} removido do estoque.")
    else:
        print(f"{nome} não encontrado no estoque.")

def atualizar_quantidade(nome, quantidade):
    if nome in estoque:
        estoque[nome] = quantidade
        print(f"Quantidade de {nome} atualizada para {quantidade}.")
    else:
        print(f"{nome} não encontrado no estoque.")

def listar_estoque():
    print("\nEstoque Atual:")
    for produto, quantidade in estoque.items():
        print(f"{produto}: {quantidade} unidades")
    print("-" * 30)

# Exemplo de uso
adicionar_produto("Teclado", 10)
adicionar_produto("Mouse", 5)
listar_estoque()

atualizar_quantidade("Mouse", 7)
remover_produto("Teclado")
listar_estoque()
