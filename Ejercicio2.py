def no_space(texto):
    ntext = ""
    texto = texto.lower()
    for i in texto:
        if i != " ":
            ntext += i
    return ntext

def reverse(texto):
    textorev = ""
    for i in texto:
        textorev = i + textorev
    return textorev

def es_palindromo(texto):
    texto = no_space(texto)
    txtrev = reverse(texto)
    return texto == txtrev


print("Abba", es_palindromo("Abba"))
print("Amo la paloma", es_palindromo("Amo la paloma"))
print("Hola Mundo", es_palindromo("Hola Mundo"))