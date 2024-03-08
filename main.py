print('Hugo Emilio Nomura - 22.123.051-9')
print('Paulo Hudson - 22.222.013-9')
print('Pedro Satoru Takashi - ')                # adicionar RA
print('Vitor Monteiro Vianna - 22.223.085-6')

# Descrição breve do trabalho
print("""- Objetivo:  Estudo das ondas eletromagnéticas com programação em linguagem Python.
      - Conceitos fisicos - 
      - Calculos disponiveis - 
      - limitacoes - 
      - Outra informacoes - """)

# Menu
print('______________________________________________________')

# variaveis globais
c = 3 * 10 ** 8  # velocidade da luz
f = 0  # frequencia
l = 0  # comprimento de onda
Em = 0  # campo eletrico
Bm = 0  # campo magnetico
k = 0  # numero de onda
I = 0  # intensidade
w = 0  # frequencia angular
op = 0  # opcao do menu
pi = 3.14159265358979323846
u = 4 * pi * 10 ** (-7) # constante magnetica

# Funções
def menu():
    print('Informe os paremetros de entrada')
    print('1 - Em, Bm ou I')
    print('2 - f, l, k ou w')
    op = int(input('Opcao: '))

    seletor(op)

def seletor(op):
    if op == 1:
        print('Opcao 1')
        print('1 - Em')
        print('2 - Bm')
        print('3 - I')
        op = int(input('Opcao: '))
        if op == 1:
            Em = float(input('Informe o valor de Em: '))
            Bm = Em / c
            I = (Em ** 2) / (2 * u * c)
            print('Bm: ', Bm)
            print('I: ', I)
        elif op == 2:
            Bm = float(input('Informe o valor de Bm: '))
            Em = Bm * c
            I = (Em ** 2) / (2 * u * c)
            print('Em: ', Em)
            print('I: ', I)
        elif op == 3:
            I = float(input('Informe o valor de I: '))
            Em = (2 * c * I * u) ** 0.5
            Bm = Em / c
            print('Em: ', Em)
            print('Bm: ', Bm)
    elif op == 2:
        print('Opcao 2')
        print('1 - f')
        print('2 - l')
        print('3 - k')
        print('4 - w')
        op = int(input('Opcao: '))
        if op == 1:
            f = float(input('Informe o valor de f: '))
            l = c / f
            k = 2 * pi / l
            w = 2 * pi * f
            print('l: ', l)
            print('k: ', k)
            print('w: ', w)
        elif op == 2:
            l = float(input('Informe o valor de l: '))
            f = c / l
            k = 2 * pi / l
            w = 2 * pi * f
            print('f: ', f)
            print('k: ', k)
            print('w: ', w)
        elif op == 3:
            k = float(input('Informe o valor de k: '))
            l = 2 * pi / k
            f = c / l
            w = 2 * pi * f
            print('f: ', f)
            print('l: ', l)
            print('w: ', w)
        elif op == 4:
            w = float(input('Informe o valor de w: '))
            f = w / (2 * pi)
            l = c / f
            k = 2 * pi / l
            print('f: ', f)
            print('l: ', l)
            print('k: ', k)

# Programa principal
menu()