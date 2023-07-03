#Variable global s
s = 4
#Variable SS calculada de s 
s = int(str(s)+str(s))

#Función que calcula las potencias y envía el arreglo a ser ordenado
def calcular (array):
	array = [(entry**2) for entry in array]
	array = [entry for entry in array if entry <= s]

	array = ordenar(array)

	return array

#Función que ordena el arreglo
def ordenar (array):
	for iteration in range(0, len(array)-1):	
		for i in range(0, len(array) - 1 - iteration):
		    if (array[i]>= array[i+1]):
		        array[i], array[i + 1] = array[i + 1], array[i]
	return array
        
#main
if __name__ == '__main__':
	print(calcular([-6, -5, 0, 1, 2,  5, 6]))
	print(calcular([-2, -1]))
	print(calcular([-6, -5, 0, 5, 6]))
	print(calcular([-10, 10]))
