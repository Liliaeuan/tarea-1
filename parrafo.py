cadenaLarga = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent gravida euismod lorem non convallis. Pellentesque convallis iaculis sem, nec aliquet nulla. Integer quis rutrum sem. Donec orci dolor, vestibulum ut dictum vel, ultrices vel tellus. Vivamus blandit lobortis elit, id interdum tortor sodales tempus. Maecenas ut ante nec leo ultricies sollicitudin. Vivamus tempus leo quis odio dignissim tristique. Nam lorem ex, euismod in vestibulum id, laoreet ut arcu. Suspendisse scelerisque, mi a auctor dapibus, ipsum sem tincidunt est, porta elementum enim sem et massa.

Donec arcu urna, mattis ut mollis suscipit, pulvinar elementum sem. Praesent lacus nulla, ultricies vel orci ac, luctus dapibus metus. Pellentesque hendrerit mollis est. Maecenas leo tortor, viverra at magna id, consequat bibendum massa. Donec sit amet risus in sem vestibulum mollis. In sodales leo tellus, venenatis tincidunt nisl feugiat eu. Aliquam in pellentesque turpis. Nunc gravida diam a lectus sollicitudin ornare. Proin non eros quis odio pretium convallis. In pretium laoreet felis et tristique.

Maecenas rhoncus placerat dolor, in finibus nibh dictum sit amet. Sed malesuada condimentum ipsum, ut lacinia massa fermentum eu. Sed vel condimentum nulla, vitae gravida magna. Aliquam erat volutpat. Nam mollis tempor tempor. Vestibulum accumsan, arcu ac rhoncus commodo, augue augue interdum est, ac tincidunt ipsum urna vitae dui. Sed mollis in neque id gravida. Suspendisse in tempus eros. Nunc dignissim odio pretium ligula porta, a ultrices dui commodo. Phasellus sagittis hendrerit mauris, in faucibus lorem rutrum ac. Pellentesque posuere vulputate sem, fermentum feugiat dolor lobortis eu. Vivamus ac blandit elit, non rhoncus enim. Sed eu dapibus lacus. Praesent bibendum quam aliquam metus vestibulum commodo. Cras in dui dignissim, dapibus turpis vel, sollicitudin massa. Aenean nec risus massa.

Ut ullamcorper id libero et vestibulum. Etiam euismod massa sit amet mauris interdum consequat. Sed pharetra purus eget sodales posuere. Nulla facilisi. Donec egestas nisi ac erat tincidunt dapibus. Nulla facilisi. Nunc et metus ut metus fringilla dictum commodo sit amet risus. Cras semper odio tellus, eget molestie ipsum volutpat non. Morbi urna purus, semper non fermentum et, blandit eget diam. Duis est lectus, posuere ut metus id, egestas congue sapien. Curabitur libero est, auctor eu placerat rutrum, luctus vitae tortor. Maecenas at egestas velit. Phasellus id odio ac tellus facilisis elementum id id metus. Cras dignissim sed erat id efficitur. Nunc mauris libero, suscipit vitae ultricies sit amet, fringilla vitae ex. In nec aliquam magna.

Donec ornare nibh sit amet urna rutrum mollis. Praesent non ligula ut mi sollicitudin volutpat. Aliquam eu tellus velit. Cras ipsum velit, convallis vitae est sed, euismod sodales enim. Sed eget interdum risus, vel iaculis nisl. Fusce at porttitor risus, vitae pretium metus. Nunc sit amet felis sem. Phasellus ut pretium quam. Vivamus sed consequat turpis. Maecenas ullamcorper erat nunc, ac molestie leo tempus in. Interdum et malesuada fames ac ante ipsum primis in faucibus. Aenean et eleifend nunc. Mauris magna tellus, maximus eget suscipit a, tincidunt eget justo.
"""

print(cadenaLarga)
letras = ['abcdefghijklmnñopqrstuvwxyz']
caracteres = ['a', 'e', 'i', 'o', 'u', '', ',' '.','p']
estadisticas = ['Total de caracteres:', 'Total de letras:','Total de vocales a :','Total de vocales e :','Total de vocales i :','Total de vocales o :','Total de vocales u :','Total de espacios :','Total de comas :', 'Total de puntos : ']
totales = [0,0,0,0,0,0,0,0,0,0]

#Contar el número de caracteres de la cadena larga.
totales[0] = len(cadenaLarga)
print(totales[0])
#Contar el númerode letrasde la acdena larga o de caracteres de la cadena larga.
for i in cadenaLarga:
    if i.lower() in letras[0].lower():  #L esta en letras? lwer es para mayuscula 
        totales[1] += 1
    for j in range(2, len(estadisticas)):
        if i.lower() in caracteres[j-2]:
            totales[j] += 1

print("Estadistica")
for i in range(len(estadisticas)):
    print(estadisticas[i], ':',totales[i])


#Dada una cadena larga (lorem ipsum de 5 párrafos)
#resentar un resumen de las estadísticas de los párrafos

#Total de caracteres:
#Total de letras (incluyendo vocales) :
#Total de vocales :
#Total de vocales a :
#Total de vocales e :
#Total de vocales i :
#Total de vocales o :
#Total de vocales u :
#Total de espacios :
##Total de comas :
#Total de palabras :

# Definición del código aeronáutico
codigo = [['A','ALFA'], ['B','BRAVO'], ['C','CHARLIE'], ['D','DELTA'], ['E','ECHO'],
          ['F','FOXTROT'], ['G','GOLF'], ['H','HOTEL'], ['I','INDIA'], ['J','JULIETT'],
          ['K','KILO'], ['L','LIMA'], ['M','MIKE'], ['N','NOVEMBER'], ['O','OSCAR'],
          ['P','PAPA'], ['Q','QUEBEC'], ['R','ROMEO'], ['S','SIERRA'], ['T','TANGO'],
          ['U','UNIFORM'], ['V','VICTOR'], ['W','WHISKEY'], ['X','XRAY'], ['Y','YANKEE'],
          ['Z','ZULU']]

# Función para convertir un código en su forma extendida
def convertir_codigo(codigo, codigo_ingresado):
    extendido = []
    for letra in codigo_ingresado:
        for code in codigo:
            if letra.upper() == code[0]:
                extendido.append(code[1])
                break
    return extendido

# Solicitar al usuario ingresar un código
codigo_ingresado = input("Ingrese el código: ")

# Mostrar el código aeronáutico extendido
print("El código aeronáutico extendido es:", ' '.join(convertir_codigo(codigo, codigo_ingresado)))
