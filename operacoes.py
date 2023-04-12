v1 = int(input())
v2 = int(input())
def operacoes(valor_1,valor_2):
    caractere = int(input())
    if caractere == 1:
        op = v1+v2
        return(op)
    elif caractere == 2:
        op = v1-v2
        return(op)
    elif caractere == 3:
        op = v1*v2
        return(op)
    elif caractere ==4:
        op = v1/v2
        return(op)
print(operacoes(v1,v2))


