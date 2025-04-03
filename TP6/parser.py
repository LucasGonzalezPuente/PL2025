import re

class Analizador:
    def __init__(self, expresion):
        self.tokens = re.findall(r'\d+|[-+*/()^]', expresion.replace(" ", ""))
        self.token_actual = None
        self.siguiente_token()

    def siguiente_token(self):
        if self.tokens:
            self.token_actual = self.tokens.pop(0)
        else:
            self.token_actual = None

    def analizar(self):
        return self.analizarE()

    def analizarE(self):
        """E -> T { (+ | -) T }*"""
        resultado = self.analizarT()
        while self.token_actual in ('+', '-'):
            operador = self.token_actual
            self.siguiente_token()
            derecha = self.analizarT()
            if operador == '+':
                resultado += derecha
            elif operador == '-':
                resultado -= derecha
        return resultado

    def analizarT(self):
        """T -> F { (* | /) F }*"""
        resultado = self.analizarF()
        while self.token_actual in ('*', '/'):
            operador = self.token_actual
            self.siguiente_token()
            derecha = self.analizarF()
            if operador == '*':
                resultado *= derecha
            elif operador == '/':
                resultado /= derecha
        return resultado

    def analizarF(self):
        """F -> ( E ) | número"""
        if self.token_actual == '(':
            self.siguiente_token()
            resultado = self.analizarE()
            if self.token_actual == ')':
                self.siguiente_token()
            else:
                raise SyntaxError("Se esperaba un ')'")
            return resultado
        elif self.token_actual.isdigit():
            return self.analizarNumero()
        else:
            raise SyntaxError(f"Token inesperado: {self.token_actual}")

    def analizarNumero(self):
        """Reconoce números enteros"""
        resultado = int(self.token_actual)
        self.siguiente_token()
        return resultado


def calcular_expresion(expresion):
    analizador = Analizador(expresion)
    return analizador.analizar()


# Ejemplos de uso
expresion1 = "2+3"
expresion2 = "67-(2+3*4)"
expresion3 = "(9-2)*(13-4)"

print(f"Resultado de {expresion1}: {calcular_expresion(expresion1)}")
print(f"Resultado de {expresion2}: {calcular_expresion(expresion2)}")
print(f"Resultado de {expresion3}: {calcular_expresion(expresion3)}")
