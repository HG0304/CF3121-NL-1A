print('Hugo Emilio Nomura - 22.123.051-9')
print('Paulo Hudson - 22.222.013-9')
print('Pedro Satoru Takashi - 22.123.019-6')                
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
    print('\n=======================================')
    print('Selecione uma opção:')
    print('---------------------------------------')
    print('1. Calcular Em , Bm  ou I ')
    print('2. Calcular f , l , k  ou w ')
    print('0. Sair')
    print('=======================================')
    op = int(input('Opcao: '))

    seletor(op)

#Proprio Float já faz a interpretação de núemeros científicos.

def seletor(op):
    if op == 1:
        print('1 - Em (Amplitudo do Campo Elétrico)')
        print('2 - Bm (Amplitudo do Campo Magnético)')
        print('3 - I  (Intensidade da onda eletromagnética)')
        print('=======================================')
        op = int(input('Opcao: '))
        if op == 1:  #teste correto
            Em = float(input('Informe o valor de Em: '))
            Bm = Em / c
            I = (Em ** 2) / (2 * u * c)
            print('Bm: {:.2e}'.format(Bm))
            print('I: {:.2e}'.format(I))
        elif op == 2: #teste correto, mas lembrar de mudar as unidades de medida para cada caso
            Bm = float(input('Informe o valor de Bm: '))
            Em = Bm * c
            I = (Em ** 2) / (2 * u * c)
            print('Em: {:.2e}'.format(Em))
            print('I: {:.2e}'.format(I))
        elif op == 3:  #teste correto
            I = float(input('Informe o valor de I: '))
            Em = (2 * c * I * u) ** 0.5
            Bm = Em / c
            print('Em: {:.2e}'.format(Em))
            print('Bm: {:.2e}'.format(Bm))
    elif op == 2:
        print('1 - f (Frequencia)')
        print('2 - l (Número de onda)')
        print('3 - k (Comprimento de onda)')
        print('4 - w (Frequencia Angular)')
        print('=======================================')
        op = int(input('Opcao: '))
        if op == 1: #teste correto
            f = float(input('Informe o valor de f: '))
            l = c / f
            k = 2 * pi / l
            w = 2 * pi * f
            print('k: {:.2e}'.format(l))
            print('l: {:.2e}'.format(k))
            print('w: {:.2e}'.format(w))
        elif op == 2:  # teste correto
            l = float(input('Informe o valor de l: '))
            k = 2 * pi / l
            f = c / k
            w = 2 * pi * f
            print('f: {:.2e}'.format(f))
            print('k: {:.2e}'.format(k))
            print('w: {:.2e}'.format(w))
        elif op == 3: #Teste correto
            k = float(input('Informe o valor de k: '))
            l = 2 * pi / k
            f = c / k
            w = 2 * pi * f
            print('f: {:.2e}'.format(f))
            print('l: {:.2e}'.format(l))
            print('w: {:.2e}'.format(w))
        elif op == 4:    #teste correto
            w = float(input('Informe o valor de w: '))
            f = w / (2 * pi)
            l = c / f
            k = 2 * pi / l
            print('f: {:.2e}'.format(f))
            print('k: {:.2e}'.format(l))
            print('l: {:.2e}'.format(k))
            
# Programa principal
menu()
