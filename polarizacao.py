import math

# Função para exibir os nomes dos autores
def autores():
    print("----------------------")
    print("1. Mario Eugenio Silva")
    print("2. Kaynã de Deus")
    print("----------------------")
    print()


def intro():
    print("Bem-vindo ao Programa sobre Polarização da Luz!")
    print("Neste programa, você irá calcular a intensidade da luz que passa por um filtro polarizador.")
    print()
    print("A polarização da luz refere-se ao alinhamento das ondas eletromagnéticas, e é usada em diversas aplicações, como óculos de sol polarizados, fotografia e física.")
    print("A polarização da luz basicamente é filtrar as direções de propagação da onda elétrica da onda elétromagnética da luz, desse modo diminuindo sua intensidade ou até")
    print("Filtrando ela totalmente até não passar mas luz nenhuma")
    print("Neste programa, você poderá calcular a intensidade da luz transmitida por um filtro polarizador, considerando a Lei de Malus.")
    print()


def calcular_intensidade(I0, theta):
    theta_rad = math.radians(theta)
    return I0 * math.cos(theta_rad)**2

# Parte 1: Estudo com 2 polarizadores
def estudo_2_polarizadores():
    print("2 Polarizadores")
    
    I0 = float(input("Informe a intensidade inicial I0 em Watts (W): "))
    theta1 = float(input("Informe o ângulo θ1 (primeiro polarizador) em graus: "))
    theta2 = float(input("Informe o ângulo θ2 (segundo polarizador) em graus: "))

    I1 = calcular_intensidade(I0, theta1)
    I2 = calcular_intensidade(I1, theta2)
    
    print(f"Intensidade após o primeiro polarizador (I1): {I1:.2f} W")
    print(f"Intensidade após o segundo polarizador (I2): {I2:.2f} W")

    # Parte 1b: Entrada: I1, θ1, θ2; Saída: I0 e I2
    print("\n1b. Entrada: I1, θ1, θ2; Saída: I0 e I2")
    I1 = float(input("Informe a intensidade I1 (em Watts): "))
    theta1 = float(input("Informe o ângulo θ1 em graus: "))
    theta2 = float(input("Informe o ângulo θ2 em graus: "))
    
    # Calculando I0
    I0 = I1 / math.cos(math.radians(theta1))**2
    
    # Calculando I2
    I2 = I1 * math.cos(math.radians(theta2))**2
    
    print(f"Intensidade inicial (I0): {I0:.2f} W")
    print(f"Intensidade após o segundo polarizador (I2): {I2:.2f} W")


def estudo_3_polarizadores():
    print("\n---- Estudo com 3 Polarizadores ----")
    print("2a. Entrada: I0, θ1, θ2, θ3; Saída: I1, I2, I3")
    I0 = float(input("Informe a intensidade inicial I0 em Watts (W): "))
    theta1 = float(input("Informe o ângulo θ1 em graus: "))
    theta2 = float(input("Informe o ângulo θ2 em graus: "))
    theta3 = float(input("Informe o ângulo θ3 em graus: "))

    I1 = calcular_intensidade(I0, theta1)
    I2 = calcular_intensidade(I1, theta2)
    I3 = calcular_intensidade(I2, theta3)

    print(f"Intensidade após o primeiro polarizador (I1): {I1:.2f} W")
    print(f"Intensidade após o segundo polarizador (I2): {I2:.2f} W")
    print(f"Intensidade após o terceiro polarizador (I3): {I3:.2f} W")

    print("\n2b. Entrada: I1, θ1, θ2, θ3; Saída: I2, I3 e I0")
    I1 = float(input("Informe a intensidade I1 (em Watts): "))
    theta1 = float(input("Informe o ângulo θ1 em graus: "))
    theta2 = float(input("Informe o ângulo θ2 em graus: "))
    theta3 = float(input("Informe o ângulo θ3 em graus: "))
    
    # Calculando I2
    I2 = I1 * math.cos(math.radians(theta2))**2
    
    # Calculando I3
    I3 = I2 * math.cos(math.radians(theta3))**2
    
    # Calculando I0
    I0 = I1 / math.cos(math.radians(theta1))**2
    
    print(f"Intensidade após o segundo polarizador (I2): {I2:.2f} W")
    print(f"Intensidade após o terceiro polarizador (I3): {I3:.2f} W")
    print(f"Intensidade inicial (I0): {I0:.2f} W")

    # Parte 2c: Entrada: I2, θ1, θ2, θ3; Saída: I1, I3 e I0
    print("\n2c. Entrada: I2, θ1, θ2, θ3; Saída: I1, I3 e I0")
    I2 = float(input("Informe a intensidade I2 (em Watts): "))
    theta1 = float(input("Informe o ângulo θ1 em graus: "))
    theta2 = float(input("Informe o ângulo θ2 em graus: "))
    theta3 = float(input("Informe o ângulo θ3 em graus: "))
    
    # Calculando I1 a partir de I2 e θ2
    I1 = I2 / math.cos(math.radians(theta2))**2
    
    # Calculando I3 a partir de I2 e θ3
    I3 = I2 * math.cos(math.radians(theta3))**2
    
    # Calculando I0 a partir de I1 e θ1
    I0 = I1 / math.cos(math.radians(theta1))**2
    
    print(f"Intensidade após o primeiro polarizador (I1): {I1:.2f} W")
    print(f"Intensidade após o terceiro polarizador (I3): {I3:.2f} W")
    print(f"Intensidade inicial (I0): {I0:.2f} W")

    # Parte 2d: Entrada: I3, θ1, θ2, θ3; Saída: I0, I1, I2
    print("\n2d. Entrada: I3, θ1, θ2, θ3; Saída: I0, I1, I2")
    I3 = float(input("Informe a intensidade I3 (em Watts): "))
    theta1 = float(input("Informe o ângulo θ1 em graus: "))
    theta2 = float(input("Informe o ângulo θ2 em graus: "))
    theta3 = float(input("Informe o ângulo θ3 em graus: "))
    
    # Calculando I2
    I2 = I3 / math.cos(math.radians(theta3))**2
    
    # Calculando I1
    I1 = I2 / math.cos(math.radians(theta2))**2
    
    # Calculando I0
    I0 = I1 / math.cos(math.radians(theta1))**2
    
    print(f"Intensidade inicial (I0): {I0:.2f} W")
    print(f"Intensidade após o primeiro polarizador (I1): {I1:.2f} W")
    print(f"Intensidade após o segundo polarizador (I2): {I2:.2f} W")


def menu():
    while True:
        print("Menu:")
        print("1. Estudo com 2 polarizadores")
        print("2. Estudo com 3 polarizadores")
        print("3. Sair")

        escolha = input("Escolha uma opção (1-3): ")

        if escolha == '1':
            estudo_2_polarizadores()
        elif escolha == '2':
            estudo_3_polarizadores()
        elif escolha == '3':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Função para rodar o programa
def rodar_programa():
    exibir_autores()  # Exibe os autores
    exibir_intro()    # Exibe a introdução sobre o programa
    menu()            # Exibe o menu para interagir com o programa

# Executando o programa
if __name__ == "__main__":
    rodar_programa()
