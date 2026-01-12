


def impar_ou_par():
    numer = int(input("Digite o numero: "))
    if(numer % 2 == 0):
        return "par"
    else:
        return "Impar"
    

def definir_idade():
    idade = int(input("Digite sua idade: "))
    if(idade<= 12):
        return "Criança"
    elif(idade<=18):
        return "Adolescente"
    else:
        return "Adulto"

def verifica_senha(senha, usuario):
    senha_correta = 1234
    usuario_correto = "Andre"
    if(senha == senha_correta and usuario == usuario_correto):
        return "Conectado com sucesso"
    else:
        return("Falha na conexão")



def plano_cartesiano(x,y):
    if(x> 0 and y>0):
        return "Primeiro Quadrante"
    elif(x<0 and y> 0):
        return "Segundo Quadrante"
    elif(x<0 and y<0):
        return "Terceiro Quadrante"
    elif(x>0 and y<0):
        return "Quarto Quadrante"
    else:
        return "O ponto esta localizado no eixo de origem"


def main():
     resultado = impar_ou_par()
     print(resultado)

     categoria_idade = definir_idade()
     print(categoria_idade)

     usuario = input("Usuario: ")
     senha = int(input("Senha: "))
     autentificacao = verifica_senha(senha,usuario)
     print(autentificacao)

     x = int(input("Digite o eixo X: "))
     y = int(input("Digite o eixo Y: "))
     quadrante = plano_cartesiano(x,y)
     print(quadrante)


     


if __name__ == "__main__":
    main()
