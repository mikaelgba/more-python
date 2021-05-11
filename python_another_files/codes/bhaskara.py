def bhaskara(a, b, c):

    delta = (b ** 2) - (4 * a * c)
    x1 = (-b + delta ** (1/2)) / (2 * a)
    x2 = (-b - delta ** (1/2)) / (2 * a)

    print('\nValor de DELTA: {:.2f}'.format(delta))
    print('\nValor de X1: {:.2f}'.format(x1))
    print('\nValor de X2: {:.2f}'.format(x2))

if __name__ == '__main__':

    while(True):
        
        print("Equação de 2º Grau: ")
        a = float(input("Digite o valor de A: "))
        b = float(input("Digite o valor de B: "))
        c = float(input("Digite o valor de C: "))
        bhaskara(a, b, c)

        outra = input("\nDeseja fazer outra equação? digite s para Sim")
        if(outra != 's'): break

        
        
