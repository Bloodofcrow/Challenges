#Variable goblal s
s = 4

#Función que elimina los número iguales o mayores a s en el arreglo y lo reordena
def calcular(array):

    arrayToStr = ' '.join([str(elem) for elem in array])

    for entry in arrayToStr:
        if entry != ' ' :
            if int(entry) >= s: arrayToStr = arrayToStr.replace(entry, "")

    arrayToStr = arrayToStr.split(' ')

    nArray = [int(entry) for entry in arrayToStr if entry != '']
    nArray = nArray[::-1]

    return nArray

#main
if __name__ == '__main__':
    print(calcular([1, 2, 3, 4, 5, 6]))
    print(calcular([10, 20, 30, 40]))  
    print(calcular([6]))  
    print(calcular([66]))  
    print(calcular([65]))  
    print(calcular([6, 2, 1]))  
    print(calcular([60, 6, 5, 4, 3, 2, 7, 7, 29, 1])) 