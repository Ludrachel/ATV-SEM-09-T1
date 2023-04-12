def diferenca(v1,v2,v3):
    v2_diferenca = abs(v2 - v1)
    v3_diferenca = abs(v3 - v1)
    return v2_diferenca if v2_diferenca < v3_diferenca else v3_diferenca
def main():
    valor_1 = int(input())
    valor_2 = int(input())
    valor_3 = int(input())

    menor_diferenca = diferenca(valor_1,valor_2,valor_3)
    print(menor_diferenca)
if __name__ == '__main__':
    main()
    
    
    
