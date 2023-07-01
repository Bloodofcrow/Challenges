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
    print(calcular([1,24,3,5,6,152]))