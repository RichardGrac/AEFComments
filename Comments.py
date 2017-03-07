# print("Hola mundo")
archivo = open("Input.txt")
linea = archivo.read()
archivo.close()
#Imprimimos el texto
#print (linea)

estado = 1
cont_inicial = 0
contador = 0
band = True
lineaActual = 1

while contador < len(linea):
    caracter = linea[contador]
    if caracter == '\n':
        lineaActual += 1
        contador += 1
        continue

    #INICIO DE AUTÓMATA
    if (estado == 1):
        if caracter == '/':
            estado = 2
        elif (caracter == ' ') | (caracter == '\t') | (caracter == '\n'):
            estado = 1
        else:
            estado = 0 #Estado de Error
    elif estado == 2:
        if caracter == '*':
            estado = 3
        elif caracter == '/':
            estado = 1 #Forma de terminar
            while (contador < len(linea)) & (linea[contador] != '\n'):
                contador += 1
            lineaActual += 1
            print("Comment inline detected: " + linea[cont_inicial+1:contador])
            cont_inicial = contador
        else:
            estado = 0
    elif estado == 3:
        if caracter == '*':
            estado = 4
    elif estado == 4:
        if caracter == '/':
            estado = 1 #Terminó, volvemos al estado inicial
            print("Comment detected: " + linea[cont_inicial:contador+1])
            cont_inicial = contador
            cont_inicial += 1
        elif caracter == '*':
            estado = 4
        else:
            estado = 3

    if estado == 0:
       band = False
       break
    contador += 1
    #FIN DE AUTÓMATA (while)

#Si está en estado de error 0 ó si quedó en un estado NO TERMINANTE:
if (estado == 0) | ((estado != 4) & (estado != 1)):
    print("Error en linea", lineaActual)
    band = False
# Si todo salió bien:
if band:
    print("Without problems.")





