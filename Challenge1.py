s = 4

def examinar (number):
  cadena = str(number)
  for entry in cadena:
    if int(entry) >= s: cadena = cadena.replace(str(entry), "")
  return cadena

def recorrer (array):
  newArray = []
  for number in array:
    temporal = examinar(number)
    if temporal != '':
      newArray.insert(0, int(temporal))
  return newArray

if __name__ == '__main__':
  print (recorrer([10, 20, 30, 40]))
