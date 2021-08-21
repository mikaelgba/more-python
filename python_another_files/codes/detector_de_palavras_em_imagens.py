import easyocr

def test():
    leitor = easyocr.Reader(['pt'])
    resultados = leitor.readtext('images/dbg.png', paragraph=False)

    for palavra in resultados:
        print(f'Palavra: {palavra[0]}\n'
          f'Posição em relação a imagem: {palavra[1]}\n')

if __name__ == '__main__':
    test()