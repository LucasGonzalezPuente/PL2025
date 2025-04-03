# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 19:51:33 2025

@author: Lucas González Puente
"""
import sys

# Solicitar texto al usuario
texto_entrada = input("Introduce el texto de entrada: ")

def somador_on_off(texto):
    soma = 0
    ativo = True
    numero_actual = ''
    resultado = []
    i = 0

    while i < len(texto):
        char = texto[i]

        # Control On/Off (case-insensitive) sin alterar la salida
        if texto[i:i+2].lower() == 'on':
            ativo = True
            resultado.append('On')
            i += 2
            continue
        elif texto[i:i+3].lower() == 'off':
            ativo = False
            resultado.append('Off')
            i += 3
            continue

        # Procesamiento de dígitos
        if char.isdigit():
            numero_actual += char
        else:
            if numero_actual:
                resultado.append(numero_actual)
                if ativo:
                    soma += int(numero_actual)
                numero_actual = ''

            if char == '=':
                resultado.append(' = ')  # Mantener un espacio antes y después del signo
                resultado.append(f'>> {soma}')
            else:
                resultado.append(char)

        i += 1

    # Suma final de número pendiente
    if numero_actual:
        resultado.append(numero_actual)
        if ativo:
            soma += int(numero_actual)

    # Mostrar suma final al final del texto
    resultado.append(f'\n>> {soma}')

    return ''.join(resultado)

# Salida del resultado
print(somador_on_off(texto_entrada))
