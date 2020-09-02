def menu():
    print("O que você deseja? \n1) Criptografia \n2) Decriptografia")
    escolha = input(">>>")
    if escolha == '1':
        frase = input("Digite digite a string: ")
        cifra = int(input("Digite o valor de rotação entre 1 e 9: "))
        cripto(frase, cifra)
    elif escolha == '2':
        decripto()
    else:
        print("Opção inválida")
        menu()
        
def cripto(frase, cifra):
    mensagem_cifra= []
    arquivo = open("Cripto.txt", "a+")
    arquivo.writelines(str(cifra)+'\n')
    for letra in frase:
        if letra == ' ':
            mensagem_cifra.append(letra)
        else:
            l = ord(letra)+cifra
            mensagem_cifra.append(chr(l))
    arquivo.writelines(''.join(mensagem_cifra))
    arquivo.close()
    
def decripto():
    mensagem = []
    arquivo = open("Cripto.txt", 'r')
    rota = int(arquivo.read(1))
    frase = arquivo.read().strip()
    for letra in frase:
        if letra == ' ':
            mensagem.append(letra)
        else:
            mensagem.append(chr(ord(letra)- rota))
            
    print(''.join(mensagem))
    
print("Testando")
menu()
