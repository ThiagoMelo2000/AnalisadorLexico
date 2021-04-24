def teste(palavra):
    
    reservada = ['if', 'else', 'def', 'print', 'for', 'while', 'int']
    numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    
    if (''.join(palavra) in reservada):
        
        return print(''.join(palavra) + ' = palavra reservada \n')
    
    elif(''.join(palavra[0]) in numeros):
        
        return print(''.join(palavra) + ' = número \n')
    
    else:
        
        return print(''.join(palavra) + ' = texto \n')
    


texto = open('arquivo.txt', 'r')

lista = texto.readlines()

aux = list()

lista_simb = list()
lista_palavra = list()

simbolos = ['.', ',', '=', '!', '(', ')', '%', '*', '+', '-', '/', '<', '>', ' ']    

for linha in lista:
    
    for item in linha:
    
        aux.append(item)
        
        
for palavra in aux:
    
    if(palavra in simbolos):
        
        if(len(lista_palavra) != 0):
            
            teste(lista_palavra)
           
            lista_palavra.clear()
            
        
        print(''.join(palavra) + ' = simbolo \n')
        
    else:
        
        lista_palavra.append(palavra)

    
texto.close()