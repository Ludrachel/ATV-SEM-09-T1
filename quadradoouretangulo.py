base = int(input())
altura = int(input())

def verificar(b,h):
    if b == h:
        print("QUADRADO")
    else:
        perimetro = 2*(b+h)
        area = b * h
        print(f'{perimetro} - {area}')
verificar(base,altura)

