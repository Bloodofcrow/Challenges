#Función que evalúa el menor valor que no se puede generar
def calcular(array):
    array.sort()
    posible = 1  

    for index in array:
        if index > posible:
            return posible  
        posible += index

    return posible + 1 

#main
if __name__ == '__main__':
	print(calcular([6, 1, 1, 2, 22]))  
	print(calcular([1, 1, 1, 1, 1, 2]))
	print(calcular([1, 5, 1, 1, 1, 10, 15, 20, 100]))