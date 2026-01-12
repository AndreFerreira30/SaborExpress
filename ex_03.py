numeros = [1,2,3,4,5,6,7,8,9,10]
nomes = ["André", "Cristina", "Ester", "Estefane"]
anos = [2003,2026]



# EX 1 - Percorrendo listas
for num in numeros:
    print(num)

for nom in nomes:
    print(nom)

for ano in anos:
    print(ano)

#EX 2 - calculando numeros impares
def calcular_impares(lista_de_numeros):
    soma = 0
    for numeros in lista_de_numeros:
        if numeros % 2 == 1:
            soma += numeros
    return soma

#EX 3 - imprimir em ordem decrescente
def ordem_decrescente(lista_de_numeros):
    n = len(lista_de_numeros) -1
    while n>= 0:
        print (lista_de_numeros[n])
        n = n - 1

#EX 4 - Tabuada
def tabuada(numero):
    for i in range(11):
        print(numero, " x ", i, " = ",(numero*i))


#EX 6 - somar total da lista
def calcularElementos(lista_numeros):
    soma = 0
    try:
        for n in lista_numeros:
            soma += n
    except:
        print("Houve um erro ao calcular a lista")
        soma = -1
    return soma


#EX 7 - calcular media da lista
def calcularMedia(lista_numeros):
    soma = 0
    media = 0
    try:
        for n in lista_numeros:
            soma += n
        media = soma / len(lista_numeros)
    except ZeroDivisionError:
            print("A lista está vazia, não é possível calcular a média.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    return media
    

def main():
    resultado = calcular_impares(numeros)
    print(resultado)

    ordem_decrescente(numeros)

    tabuada(5)

    resp = calcularElementos(numeros)
    print(resp)
    #Testando o tratamento de erros;
    outra_lista = [1,"2",2,3,4]
    res = calcularElementos(outra_lista)
    print(res)


    media = calcularMedia(numeros)
    print(media)
    #Testando o tratamento de erros;
    nlista  = []
    media = calcularMedia(nlista)
    print(media)







if __name__ == "__main__":
    main()