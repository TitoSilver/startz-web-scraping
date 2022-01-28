lista = [1,8,26,4,2,9,45,33,52,11,18,13]

# En base a la lista informada

#Crear una lista llamada "Par", agregando de la lista original los números pares

#Crear una lista llamada "Impar", agregando de la lista original los números impares

#Imprimir la cantidad y la suma de elementos de la lista inicial

par=[]
impar=[]

for element in lista:
    if element %2==0:
        par.append(element)
    else:
        impar.append(element)

print("Cant element \nPar: {}\nImpar: {}".format(len(par),len(impar)))

print("Total sum \nPar: {}\nImpar: {}".format(sum(par),sum(impar)))