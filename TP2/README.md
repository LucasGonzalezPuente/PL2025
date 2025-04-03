**1. parse_line(line)**<br> 
Esta función recibe una línea del CSV y la divide en campos correctamente, respetando los ; que están dentro de comillas.  

**2. 2. main()**<br>
La función principal que organiza el resto del trabajo:<br>  

: compositores = set()<br>  
Usamos un set para guardar compositores sin duplicados.<br>  
<br>
: map_obras_periodo = {}<br>  
Es un diccionario con:<br>  

Clave: el período (Ej: 'Barroco', 'Clássico')<br>  

Valor: un conjunto (set) con las obras únicas de ese período.<br>

**3. Saltar la primera línea (el header del CSV).**<br>  
Lee cada línea (una por obra), la limpia y la pasa a parse_line.<br>  

Luego, extrae de los campos:<br>  

obra = campos[0]<br>  

periodo = campos[3]<br> 

compositor = campos[4]<br>  

Y:<br>  

Añade el compositor al conjunto.<br>  

Añade la obra al conjunto de obras del período correspondiente.<br>  

**4. Impresion de resultados**  
