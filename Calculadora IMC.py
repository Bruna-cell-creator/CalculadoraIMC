def calcular_imc(peso, altura):
    """Calcula o Índice de Massa Corporal (IMC)"""
    return peso / (altura ** 2)


def obter_categoria(imc):
    """Retorna a categoria de peso com base no IMC"""
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 24.9 <= imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidade"


def obter_peso():
    """Solicita e retorna o peso do usuário em kg"""
    while True:
        try:
            peso = float(input("Digite seu peso em kg: "))
            if peso > 0:
                return peso
            else:
                print("Por favor, digite um peso válido.")
        except ValueError:
            print("Entrada inválida. Digite um número para o peso.")


def obter_altura():
    """Solicita e retorna a altura do usuário em metros"""
    while True:
        try:
            altura = float(input("Digite sua altura em metros: "))
            if altura > 0:
                return altura
            else:
                print("Por favor, digite uma altura válida.")
        except ValueError:
            print("Entrada inválida. Digite um número para a altura.")


def calcular_imc_usuario():
    """Executa o programa de cálculo de IMC"""
    print("Bem-vindo à Calculadora de IMC!")

    peso = obter_peso()
    altura = obter_altura()
    imc = calcular_imc(peso, altura)
    categoria = obter_categoria(imc)

    print(f"Seu IMC é: {imc:.2f}")
    print(f"Categoria: {categoria}")


# Inicia o programa de cálculo de IMC
calcular_imc_usuario()
