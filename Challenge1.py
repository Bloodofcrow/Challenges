#Variable global s
s = 4

#Función que examina y remueve los números iguales o superiores a la variable global 
def examinar (number):
  cadena = str(number)
  for entry in cadena:
    if int(entry) >= s: cadena = cadena.replace(str(entry), "")
  return cadena

#Función que recorre el arreglo
def recorrer (array):
  newArray = []
  for number in array:
    temporal = examinar(number)
    if temporal != '':
      newArray.insert(0, int(temporal))
  return newArray

#main
if __name__ == '__main__':
  print (recorrer([10, 20, 30, 40]))
