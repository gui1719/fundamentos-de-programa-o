import calculadorabiblioteca


def main():

    print("Bem-vindo à calculadora! Digite os números e escolha as operações:")

    valor_atual = 0

    while True:
        try:
            if valor_atual == 0:
                x = int(input("Informe o primeiro número (ou '0' para sair): "))
                if x == 0:
                    print("Encerrando a calculadora.")
                    break
            else:
                x = valor_atual

            y = int(input("Informe o segundo número (caso não seja necessário, digite '0', para continuar com os cálculos): "))

            print("\nEscolha uma operação:")
            print("+ para soma")
            print("- para subtração")
            print("* para multiplicação")
            print("/ para divisão")
            print("! para fatorial do primeiro número")
            print("^ para exponenciação (x^y)")
            print("% para resto da divisão (x % y)")
            print("r para raiz quadrada do primeiro número")
            print("c para resetar a calculadora")
            print("t para desligar a calculadora")
            operação = input("Digite a operação: ")


            if operação == "+":
                resultado = calculadorabiblioteca.soma(x, y)
            elif operação == "-":
                resultado = calculadorabiblioteca.subtracao(x, y)
            elif operação == "*":
                resultado = calculadorabiblioteca.multiplicacao(x, y)
            elif operação == "/":
                resultado = calculadorabiblioteca.divisao(x, y)
            elif operação == "!":
                resultado = calculadorabiblioteca.fatorial(x)
            elif operação == "^":
                resultado = calculadorabiblioteca.exponenciacao(x, y)
            elif operação == "%":
                resultado = calculadorabiblioteca.resto(x, y)
            elif operação == "r":
                resultado = calculadorabiblioteca.raiz_quadrada(x)
            elif operação == "c":
                resultado = calculadorabiblioteca.reset()
                valor_atual = resultado
                print("Calculadora resetada.")
                continue
            elif operação == "t":
                calculadorabiblioteca.turn_off()
                break
            else:
                print("Operação inválida. Tente novamente.")
                continue

            valor_atual = resultado
            print(f"Resultado: {resultado}\n")
        except ValueError:
            print("Erro: Entrada inválida. Digite um número inteiro.")
        except Exception as e:
            print(f"Erro: {e}")


if __name__ == "__main__":
    main()
