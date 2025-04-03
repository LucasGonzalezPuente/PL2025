**1. Entrada**<br>
El usuario escribe varias líneas en formato Markdown

**2. Procesamiento**<br>
Esta función transforma ese texto a HTML.<br>
Divide el texto en líneas para procesar una por una.
  - html_lines: lista que irá acumulando las líneas convertidas a HTML.

  - in_list: para saber si estamos dentro de una lista ordenada (<ol>). <br>
**3. Conversion**<br>
Detecta si una línea empieza con #, ## o ### y los convierte en encabezados HTML
Detecta líneas que empiezan con 1., 2. etc.
Detecta **texto** y lo convierte en <b>texto</b> (negrita).

Detecta *texto* y lo convierte en <i>texto</i> (cursiva).

Limitación: solo reemplaza la primera ocurrencia, no todas.

Detecta enlaces e imagenes
Al dejar de encontrar ítems de lista, cierra el <ol> automáticamente.

**4. Salida**<br>
Imprime el HTML generado:



