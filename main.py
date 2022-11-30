vetor = list()

def inserirNum():
    global vetor
    quantidade = int(input('Para começar digite a quantidade de números que deseja adicionar: '))
    vetor = [int(input('Digite aqui: ')) for i in range(quantidade)]

inserirNum()

def iterativa():
    resultado = 0
    for i in vetor:
        resultado += i
    print(f'\n --- Resultado: {resultado} --- ')
    
def recursiva(n):
    if len(vetor) <= n:
        return 0
    return vetor[n] + recursiva(n + 1)
    
def recursiva2(vetor):
    if len(vetor) <= 0:
        return 0
    return vetor[0] + recursiva2(vetor[1:])

while True:
    selecao = input('''\n - Menu - \n
    - 1 - Recursciva
    - 2 - Interativa
    - 3 - Escolher outros números
    - 0 - Fim\n\nSelecionar: ''')
    if selecao == '0':
        break
    elif selecao == '1':
        print(f'\n --- Resultado: {recursiva(0)} ---')
    elif selecao == '2':
        iterativa()
    elif selecao == '3':
        inserirNum()