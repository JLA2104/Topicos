def mostrar_tabuada(numero):
    print(f"Tabuada do {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

def main():
    numero = int(input("Digite o número para ver a tabuada: "))
    mostrar_tabuada(numero)

if __name__ == "__main__":
    main()
