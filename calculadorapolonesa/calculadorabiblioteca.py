def soma(a, b):

    return a + b


def subtracao(a, b):

    return a - b


def multiplicacao(a, b):

    resultado = 0
    negativo = False

    if a < 0 and b > 0:
        negativo = True
        a = -a
    elif a > 0 and b < 0:
        negativo = True
        b = -b
    elif a < 0 and b < 0:
        a = -a
        b = -b

    for _ in range(b):
        resultado = soma(resultado, a)

    return -resultado if negativo else resultado


def divisao(a, b):

    if b == 0:
        return "Erro: Divisão por zero."

    resultado = 0
    negativo = False


    if a < 0 and b > 0:
        negativo = True
        a = -a
    elif a > 0 and b < 0:
        negativo = True
        b = -b
    elif a < 0 and b < 0:
        a = -a
        b = -b


    while a >= b:
        a = subtracao(a, b)
        resultado = soma(resultado, 1)

    return -resultado if negativo else resultado


def resto(a, b):

    if b == 0:
        return "Erro: Divisão por zero."

    while a >= b:
        a = subtracao(a, b)

    return a


def exponenciacao(base, expoente):

    if expoente == 0:
        return 1

    resultado = base
    for _ in range(expoente - 1):
        resultado = multiplicacao(resultado, base)

    return resultado


def fatorial(n):

    if n < 0:
        return "Erro: Fatorial de número negativo não é definido."
    if n == 0 or n == 1:
        return 1

    resultado = 1
    for i in range(1, n + 1):
        resultado = multiplicacao(resultado, i)

    return resultado


def raiz_quadrada(n):

    if n < 0:
        return "Erro: Não é possível calcular a raiz de um número negativo."

    resultado = 0
    while multiplicacao(resultado, resultado) <= n:
        resultado = soma(resultado, 1)


    return subtracao(resultado, 1)


def reset():

    return 0


def turn_off():

    print("Calculadora sendo desligada. Até a próxima!")
    exit()
