produtos = {}

while True:
    cod = int(input("Codigo: "))
    nome = input("Nome: ")
    preco = float(input("R$: "))
    qtde = int(input("Qtde: "))

    prod = []

    prod.append(nome)
    prod.append(preco)
    prod.append(qtde)
    produtos.update({cod:prod})
    resp = input("Deseja continuar: S|N? \n")
    if resp.upper() == "N":
        break

total = 0
for prod in sorted(produtos.values()):
    subtotal = prod[1] * prod[2]
    print("{} : R${:.2f}".format(prod[0], subtotal))
    total += subtotal
print(15 * "_")
print("Total: R${:.2f}".format(total))
