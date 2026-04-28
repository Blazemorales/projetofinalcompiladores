import sys
import rich

from .regex_scan import analisador_lexico

def main():
    if len(sys.argv) != 2:
        rich.print("[red b]ERRO:[/] digite lox NOME_DO_ARQUIVO <PASTA DO ARQUIVO>")
        exit(1)

    path = sys.argv[1]
    with open(path) as f:
        source = f.read()

    tokens = analisador_lexico(source)
    rich.print(tokens)
    ...
    # ast = parse(tokens)
    # inpret(ast)