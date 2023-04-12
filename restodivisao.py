def resto_divisao(n):
    resto = n % 5
    if resto == 0:
        resultado = 9*n + 7
        return resultado
    elif resto == 1:
        return "par" if n % 2 == 0 else "ímpar"
    elif resto == 2:
        resultado = 5*(n**2) - 3 * n + 42
        return resultado
    elif resto == 3:
        resultado = n // 10
        return resultado
    else:
        resultado = n**2
        return resultado
def main():
    num = int(input())
    caractere = resto_divisao(num)
    print(caractere)
if __name__ == '__main__':
    main()
            
