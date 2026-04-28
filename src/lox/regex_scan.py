import string
import re
from typing import cast
from .token import Token, classifytoken

letras = set(string.ascii_letters + "_")
numeros = set("0123456789")
alfanumericos = {*letras, *numeros}

reservados: set[classifytoken] = {
    "if",
    "else",
    "while",
    "for",
    "print",
    "class",
    "fun",
    "return",
    "this",
    "super",
    "var",
    "EOF",
}

padroes_tokens = {
    "comentario": r"//[^\n]*",
    "numero": r"\d+(\.\d+)?",
    "nome": r"[a-zA-Z_][a-zA-Z_0-9]*",
    "string": r'"[^"]*"',
    "simbolo": r"==|>=|<=|!=|[-<>+/*;={}(),.]",
    "espaco": r"[ \t]+",
    "quebra_de_linha": r"\n",
    "invalido": r".",
}

operadores_bool_none = {
    "true": True,
    "false": False,
    "nil": None,
}

tipos_operadores = {
    "true": bool,
    "false": bool,
    "nil": "nil",
}

regex_lox = re.compile(
    "|".join(f"(?P<{chave}>{valor})" for chave, valor in padroes_tokens.items())
)

def analisador_lexico(source: str) -> list[Token]:
    tokens: list[Token] = []
    linha = 1

    for i in regex_lox.finditer(source): 
        j, k = i.span()
        lexema = source[j:k]
        tipo = cast(classifytoken, i.lastgroup or "invalido")
        
        # ✅ Quebra de linha incrementa ANTES
        if tipo == "quebra_de_linha":
            linha += 1
            continue
        
        # Agora criar o token com a linha correta
        token = Token(lexema, tipo, linha)
        
        match tipo:
            case "espaco":
                # ✅ Ignorar espaços em branco
                continue
            case "comentario":
                # ✅ ADICIONAR COMENTÁRIO COMO TOKEN
                pass
            case "nome":
                if lexema in reservados:
                    token.tipo = cast(classifytoken, lexema)
                elif lexema in operadores_bool_none:
                    token.tipo = tipos_operadores[lexema]
                    token.valor = operadores_bool_none[lexema]
            case "numero":
                token.valor = float(lexema)
            case "string": 
                token.valor = lexema[1:-1]
                # ✅ Strings podem ter quebras de linha dentro
                linha += lexema.count("\n")
            case "simbolo":
                token.tipo = lexema
            case "invalido":
                token.valor = "invalid"
        
        tokens.append(token)

    tokens.append(Token("", "EOF", linha))
    return tokens