def eh_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True
def n_primos(N):
    numeros_primos = []
    numero = 2
    while len(numeros_primos) < N:
        if eh_primo(numero):
            numeros_primos.append(numero)
        numero += 1
    return numeros_primos
def main():
    N = int(input("Digite um valor inteiro N: "))
    primos = n_primos(N)
    print("N primeiros números primos:")
    print(primos)
main()