Toma como entrada una consulta tipo SPARQL y divide (tokeniza) el texto en partes llamadas tokens, clasificando cada uno según su tipo: palabra clave (SELECT, WHERE, LIMIT), variables (?x), literales ("texto"), números, identificadores, etc.

**1. El diccionario token_types define los tipos de tokens y cómo reconocerlos**:<br>

"KEYWORD": palabras clave.

"BRACE": llaves { }.

"DOT": el punto . separador de declaraciones.

"VAR": variables que comienzan con ?.

"LITERAL": cadenas de texto entre comillas "...".

"NUMBER": números enteros.

"IDENTIFIER": cualquier otra cosa no clasificada (por ejemplo, dbo:MusicalArtist o foaf:name).<br>

**2. funcion tokenize**<br>

Esta función hace todo el trabajo:

Recorre carácter por carácter la cadena de entrada.

Agrupa letras en "palabras" hasta encontrar un separador (espacio, puntuación).

Detecta comillas " para procesar literales de texto.

Llama a classify_token(word) para clasificar cada palabra encontrada.

Devuelve una lista de tuplas (tipo, valor).

**3. Funcion classify_token**<br>
Clasifica cada palabra/token según las reglas de token_types:

Si está en un conjunto (por ejemplo, KEYWORD), lo detecta directo.

Si es una función (por ejemplo, para variables o literales), evalúa la condición.

Si no encaja en ninguna categoría, se clasifica como "UNKNOWN".




