1. parse_line(line)<br> 
Esta función recibe una línea del CSV y la divide en campos correctamente, respetando los ; que están dentro de comillas.  

2. 2. main()  
La función principal que organiza el resto del trabajo:  

: compositores = set()  
Usamos un set para guardar compositores sin duplicados.  

: map_obras_periodo = {}  
Es un diccionario con:  

Clave: el período (Ej: 'Barroco', 'Clássico')  

Valor: un conjunto (set) con las obras únicas de ese período.  

3. Saltar la primera línea (el header del CSV).  
Lee cada línea (una por obra), la limpia y la pasa a parse_line.  

Luego, extrae de los campos:  

obra = campos[0]  

periodo = campos[3]  

compositor = campos[4]  

Y:  

Añade el compositor al conjunto.  

Añade la obra al conjunto de obras del período correspondiente.  

4. Impresion de resultados  
