import json

# Función para cargar el archivo JSON
def carregar_stock():
    try:
        with open('stock.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Función para guardar en un archivo JSON
def salvar_stock(stock):
    with open('stock.json', 'w') as f:
        json.dump(stock, f, indent=4)

# Función para listar los productos
def listar_produtos(stock):
    print("código | nombre      | cantidad | precio")
    print("----------------------------------------")
    for producto in stock:
        print(f"{producto['cod']} {producto['nome']} {producto['quant']} {producto['preco']:.2f}")

# Función para sumar monedas al saldo
def adicionar_moedas(saldo, monedas):
    valor_monedas = {'1e': 1.0, '50c': 0.5, '20c': 0.2, '10c': 0.1, '5c': 0.05, '2c': 0.02, '1c': 0.01}
    for moneda in monedas:
        if moneda in valor_monedas:
            saldo += valor_monedas[moneda]
    return saldo

# Función para seleccionar un producto
def selecionar_produto(stock, saldo, cod_produto):
    for producto in stock:
        if producto['cod'] == cod_produto:
            if saldo >= producto['preco']:
                if producto['quant'] > 0:
                    producto['quant'] -= 1
                    saldo -= producto['preco']
                    print(f"Puede retirar el producto dispensado \"{producto['nome']}\"")
                    return saldo
                else:
                    print("Producto fuera de stock.")
                    return saldo
            else:
                print(f"Saldo insuficiente para satisfacer su pedido")
                print(f"Saldo = {saldo:.2f}; Pedido = {producto['preco']:.2f}")
                return saldo
    print("Producto inexistente.")
    return saldo

# Función para añadir productos al stock
def adicionar_produto(stock, cod, nome, preco, quant):
    for producto in stock:
        if producto['cod'] == cod:
            producto['quant'] += quant
            print(f"Producto {nome} actualizado en stock.")
            return stock
    stock.append({"cod": cod, "nome": nome, "quant": quant, "preco": preco})
    print(f"Producto {nome} añadido al stock.")
    return stock

# Función para devolver el cambio
def dar_troco(saldo):
    troco = {}
    valores = [2.0, 1.0, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]
    for valor in valores:
        quant = int(saldo // valor)
        if quant > 0:
            troco[valor] = quant
            saldo -= quant * valor
    return troco

def imprimir_troco(troco):
    for valor, quant in troco.items():
        print(f"{quant}x {int(valor*100)}c")

# Función principal
def main():
    stock = carregar_stock()
    saldo = 0.0
    print("maq: 2024-03-08, Stock cargado, Estado actualizado.")
    print("maq: Buen día. Estoy disponible para atender su pedido.")

    while True:
        comando = input(">> ").strip().upper()

        if comando == "LISTAR":
            listar_produtos(stock)

        elif comando.startswith("MOEDA"):
            monedas = comando[6:].split(", ")
            saldo = adicionar_moedas(saldo, monedas)
            print(f"maq: Saldo = {saldo:.2f}€")

        elif comando.startswith("SELECIONAR"):
            cod_produto = comando.split()[1]
            saldo = selecionar_produto(stock, saldo, cod_produto)
            print(f"maq: Saldo = {saldo:.2f}€")

        elif comando.startswith("ADICIONAR"):
            partes = comando[9:].split(", ")
            cod = partes[0].strip()
            nome = partes[1].strip()
            preco = float(partes[2].strip())
            quant = int(partes[3].strip())
            stock = adicionar_produto(stock, cod, nome, preco, quant)

        elif comando == "SAIR":
            troco = dar_troco(saldo)
            print(f"maq: Puede retirar el cambio: ", end="")
            imprimir_troco(troco)
            print("maq: Hasta la próxima")
            salvar_stock(stock)
            break

        else:
            print("Comando inválido. Intente nuevamente.")

if __name__ == "__main__":
    main()
