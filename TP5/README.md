Permite a un usuario:

Ver el stock disponible (LISTAR)

Insertar monedas (MOEDA 1e, 50c, ...)

Comprar productos (SELECIONAR <código>)

Añadir productos nuevos o reponer stock (ADICIONAR)

Salir y recibir el cambio (SAIR)

Toda la información sobre los productos se guarda en un archivo stock.json.

**1. carregar_stock()**<br>

Carga el archivo stock.json si existe.

Si no existe, devuelve una lista vacía (stock vacío).

**2. salvar_stock**<br>

Guarda el stock actual en stock.json, de forma legible.

**3. listar_productos**<br>

Muestra el contenido actual del stock con:

Código

Nombre

Cantidad disponible

Precio

**4. adicionar_moedas**<br>

Suma el valor de monedas ingresadas al saldo actual.

**5. selecionar_produto**<br>

Permite comprar un producto:

Verifica si el código existe.

Verifica si hay stock suficiente.

Verifica si hay saldo suficiente.

Si todo está bien, descuenta precio y stock.

Muestra mensajes como:

"Puede retirar el producto dispensado "Agua""

"Saldo insuficiente para satisfacer su pedido"

**6. adicionar_produto**<br>

Permite reponer un producto ya existente o añadir uno nuevo al stock.

**7. dar_troco**<br>

Calcula el cambio a devolver usando las monedas de mayor valor posible.

**8. imprimir_troco(troco)** <br>

Imprime el cambio 

**9. main**<br>

LISTAR
Lista todos los productos.

MOEDA 1e, 50c, ...
Inserta monedas en la máquina.

SELECIONAR <código>
Intenta comprar el producto con ese código.

ADICIONAR cod, nome, preco, quant
Añade un nuevo producto o repone uno existente.

SAIR
Finaliza el programa, devuelve el cambio, y guarda el stock actualizado.

Cualquier otro comando:
Muestra mensaje de error "Comando inválido".






