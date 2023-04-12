def valores(v1,v2,v3):
    if v1==v2 and v1!=v3 and v2!=v3:
        return "Existem dois valores iguais e um diferente"
    elif v1==v3 and v1!=v2 and v2!=v3:
        return "Existem dois valores iguais e um diferente"
    elif v2==v3 and v1!=v2 and v1!=v3:
        return "Existem dois valores iguais e um diferente"
    elif v1!=v2 and v1!=v3 and v2!=v3:
        return "Todos os valores são diferentes"
    elif v1==v2 and v1==v3 and v2==v3:
        return "Todos os valores são iguais"

def main():
    num1 = int(input("digite um número : "))
    num2 = int(input("digite outro número : "))
    num3 = int(input("digite mais um número : "))

    v = valores(num1,num2,num3)
    print(v)
if __name__ == '__main__':
    main()
