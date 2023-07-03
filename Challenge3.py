#Función que ordena y envía al cálculo 
def ordenarYCalcular(array):
    array.sort()
    posible = 1  
    return(calcular(array, posible))

#Función que encuentra el menor número que no se puede generar
def calcular(array, posible):
    if array == [] : return posible
    if array[0] > posible: return posible 
    posible += array[0]
    return(calcular(array[1:], posible))

#main
if __name__ == '__main__':
	print(ordenarYCalcular([6, 1, 1, 2, 22]))  
	print(ordenarYCalcular([1, 1, 1, 1, 1]))
	print(ordenarYCalcular([1, 5, 1, 1, 1, 10, 15, 20, 100]))
