key = "11100010" #Clave de cifrado

def letra_a_binario(char:str) -> str: #Convierte cualquier caracter ASCII a un string de binarios 
    if len(char) != 1: return False
    binary_result = ''.join(format(ord(char), '08b'))
    return binary_result
def binario_a_letra(binary: str) -> str:  # Convierte un string binario de 8 bits a un caracter ASCII
    if len(binary) != 8 or not all(b in '01' for b in binary): # Validación
        return False
    char_result = chr(int(binary, 2))
    return char_result


def xorBitXBit(asciiBinary: str):
  resultado = ""
  for i,bit in enumerate(asciiBinary):
    xorBit = int(bit) ^ int(key[i]) #Se aplica ^ (XOR) de cada bit de la cadena asciiBinary y el resultado se guarda en xorBit 
    resultado+= str(xorBit)
  return resultado
def notBitXBit(asciiBinary: str):
  resultado = ""
  for bit in asciiBinary:
    resultado+= str(not int(bit)) #Simplemente inverte el bit
  
  return resultado

def cifrar_char(asciiBinary: str):
  paso1 = xorBitXBit(asciiBinary)
  return paso1
  
def descifrar_char(asciiBinary: str):
  paso1 = xorBitXBit(asciiBinary)
  return paso1

def cifrar_prompt(prompt):
  prompt_cifrado_lista = []
  for caracter in prompt:
    char_bin = letra_a_binario(caracter)
    bin_cifrado = cifrar_char(char_bin)
    prompt_cifrado_lista.append(bin_cifrado)

  prompt_cifrado = " ".join(prompt_cifrado_lista)
  return prompt_cifrado
def descifrar_prompt(prompt_cifrado):
  prompt_descifrado = ""
  for ascii_binchar in prompt_cifrado.split(" "):
    bin_descifrado = descifrar_char(ascii_binchar)
    prompt_descifrado+=binario_a_letra(bin_descifrado)
  return prompt_descifrado

while True: #Bucle infinito hasta que se haga un break (quiebre)
  print("Elija una opción\n1: cifrado\n2: descifrado\n0: cerrar programa")
  opcion = input()
  
  if not opcion.isdigit(): continue # Pasa a la siguiente iteración
  if int(opcion) == 0: break # Quiebre del programa
  if int(opcion) == 1:
    prompt = input("Ingrese el texto a cifrar ->")
    print("------------------")
    print("TEXTO CIFRADO:")
    print(cifrar_prompt(prompt))
    print("------------------")
  if int(opcion) == 2:
    print("Ingrese el texto a descfirar (verificar que el binario no tenga espacios de más, solamente los de separación)")
    prompt = input()
    print("------------------")
    print("BINARIO DESCIFRADO:")
    print(descifrar_prompt(prompt))
    print("------------------")
