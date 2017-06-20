#lista = [1, 4, 9, 16, 25]
#print(lista)

#---- Fatiando uma Lista ------#
#print(lista[0])
#print(lista[-1])
#print(lista[-3:]) #Fatia e retorna uma nova lista

#===== Concatenando uma Lista =======#
#print(lista + [32, 50, 40, 80])

#-------- Incluindo e Substituindo Na Lista --------#
'''
cubos = [1, 8, 27, 65, 125]
#cubos[3] = 64 #substitui o 65 por 64
cubos.append(216) #Adicionando ao final da lista com o metodo append
cubos.append(7 ** 3)
print(cubos)
'''
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(len(letras)) #Comprimento da Lista
letras[2:5] = ['C', 'D', 'E'] #Substituindo nas listas
print(letras)
letras[2:5] = [] #Removendo da Lista
print(letras)
letras[:] = [] #Limpando toda a Lista
print(letras)
