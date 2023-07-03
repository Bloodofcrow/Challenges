#Función que evalúa el menor valor que no se puede generar
def ordenarYCalular(array):
    array.sort()
    posible = 1  
    return(calcular(array, posible))

def calcular(array, posible):
    if array == [] : return posible + 1
    if array[0] > posible:
            return posible + 1
    posible += index
    return(calcular(array[1:], posible))

#main
if __name__ == '__main__':
	print(calcular([6, 1, 1, 2, 22]))  
	print(calcular([1, 1, 1, 1, 1]))
	print(calcular([1, 5, 1, 1, 1, 10, 15, 20, 100]))
