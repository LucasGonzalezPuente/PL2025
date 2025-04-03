# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 01:47:18 2025

@author: sistemas
"""

import string

token_types = {
    "KEYWORD": {"SELECT", "WHERE", "LIMIT"},
    "BRACE": {"{", "}"},
    "DOT": {"."},
    "VAR": lambda x: x.startswith("?"),
    "LITERAL": lambda x: x.startswith('"') and x.endswith('"'),
    "NUMBER": lambda x: x.isdigit(),
    "IDENTIFIER": lambda x: True  # Asumo que todo el resto es identificador
}

def tokenize(query: str):
    tokens = []
    word = ""
    i = 0
    while i < len(query):
        char = query[i]
        
        if char.isspace():
            if word:
                tokens.append(classify_token(word))
                word = ""
        elif char in string.punctuation and char not in {'"'}:
            if word:
                tokens.append(classify_token(word))
                word = ""
            tokens.append(classify_token(char))
        elif char == '"':
            if word:
                tokens.append(classify_token(word))
                word = ""
            end_quote = query.find('"', i + 1)
            if end_quote == -1:
                raise ValueError("String literal not closed")
            word = query[i:end_quote + 1]
            tokens.append(classify_token(word))
            word = ""
            i = end_quote
        else:
            word += char
        
        i += 1
    
    if word:
        tokens.append(classify_token(word))
    
    return tokens

def classify_token(word):
    for token_type, condition in token_types.items():
        if isinstance(condition, set):
            if word.upper() in condition:
                return (token_type, word.upper())
        elif callable(condition):
            if condition(word):
                return (token_type, word)
    return ("UNKNOWN", word)

# Ejemplo de uso
query = """SELECT ?nome ?desc WHERE {
?s a dbo:MusicalArtist.
?s foaf:name "Chuck Berry"@en .
?w dbo:artist ?s.
?w foaf:name ?nome.
?w dbo:abstract ?desc
} LIMIT 1000"""

tokens = tokenize(query)
for token in tokens:
    print(token)

