Permite evaluar expresiones matemáticas como "2+3", "67-(2+3*4)", o "(9-2)*(13-4)", respetando la precedencia de operadores.

**1. tokenizador**<br>

Convierte una expresión como "3 + (4 * 2)" separandolo en comas

Se ignoran los espacios, y se detectan números (\d+) y operadores (+, -, *, /, (, )).

**2. Analisis y evaluacion**<br>

La gramática que se sigue es similar a:


E -> T ((+|-) T)*
T -> F ((*|/) F)*
F -> (E) | número


E (expresión): suma y resta

T (término): multiplicación y división

F (factor): paréntesis o número

**analizar**

Inicia el análisis con una expresión (E)

**analizarE**

Evalúa expresiones con + y - (más bajo nivel de prioridad)

**analizarT**

Evalúa términos con * y / (más alta prioridad que + y -)

**analizarF**

Procesa factores: un número o una subexpresión entre paréntesis

**3. Evaluacion de ejemplos**<br>

Mostramos resultados de 3 ejemplos hechos









