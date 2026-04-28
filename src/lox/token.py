from typing import Literal
from dataclasses import dataclass

type classifytoken = Literal [
    "name",
    "string",
    "number",
    "bool",
    "nil",
    #condicionais
    "if",
    "else",
    "while",
    "for",
    #reservados
    "print",
    "class",
    "fun",
    "return",
    "this",
    "super",
    "var",
    #simbolos
    ";",
    "{",
    "}",
    "(",
    ")",
    "+",
    "-",
    "/",
    "*",
    #atribuicao
    "=",
    #comparacoes
    "==",
    "!=",
    ">=",
    "<=",
    ">",
    "<",
    "!",
    #end
    "EOF",
    "INVALID"
]

@dataclass
class Token:
    lexema: str
    tipo: classifytoken
    linha: int
    valor: float | bool | str | None = None
