import re
import string
from tkinter import Tk, filedialog as fd

list_tkn = []
list_err = []
data = ""


class tkn:
    def __init__(self, token, lexema, linea):
        self.token = token
        self.lexema = lexema
        self.linea = linea
        pass

    def gettoken(self):
        return self.token

    def getlexema(self):
        return self.lexema

    def getlinea(self):
        return self.linea


class err:
    def __init__(self, lexema, linea):
        self.lexema = lexema
        self.linea = linea

    def getlexema(self):
        return self.lexema

    def getlinea(self):
        return self.linea



def analizar(texto):
    global list_tkn, list_err
    list_tkn = []
    list_err = []

    palabra = ""
    estado = 0
    linea = 1

    i = 0
    while i < len(texto):
        c = texto[i]
        if estado == 0:
            # print(c)
            # ESTADO INICIAL -> signos
            if c == "~":
                palabra = palabra + c
                x = tkn("Espiral", palabra, linea)
                list_tkn.append(x)
                palabra = ""
                estado = 0
            elif c == "<":
                palabra = palabra + c
                x = tkn("Menor que", palabra, linea)
                list_tkn.append(x)
                palabra = ""
                estado = 0
            elif c == ">":
                palabra = palabra + c
                x = tkn("Mayor que", palabra, linea)
                list_tkn.append(x)
                palabra = ""
                estado = 0
            elif c == "[":
                palabra = palabra + c
                x = tkn("Corchete apertura", palabra, linea)
                list_tkn.append(x)
                palabra = ""
                estado = 0
            elif c == "]":
                palabra = palabra + c
                x = tkn("Corchete cierre", palabra, linea)
                list_tkn.append(x)
                palabra = ""
                estado = 0
            elif c == ":":
                palabra = palabra + c
                x = tkn("Puntos dobles", palabra, linea)
                list_tkn.append(x)
                palabra = ""
                estado = 0
            elif c == ",":
                palabra = palabra + c
                x = tkn("Coma", palabra, linea)
                list_tkn.append(x)
                palabra = ""
                estado = 0
            elif re.search('[a-zA-Z]', c):
                palabra += c
                estado = 1
            elif c == " " or c == "\t":
                estado = 0
            elif c == "\n":
                linea = linea + 1
                estado = 0
            elif c == "\"":
                palabra += c
                estado = 2
            else:
                palabra = palabra + c
                xer = err(palabra, linea)
                list_err.append(xer)
                palabra = ""
                estado = 0
        elif estado == 1:
            # ESTADO 1 -> letras
            if re.search("[a-zA-Z]", c):
                palabra = palabra + c
                estado = 1
            else:
                # Obtener el tipo de token
                # print(palabra)
                tipo = ""
                if palabra.lower() == "tipo":
                    tipo = "TIPO"
                elif palabra.lower() == "valor":
                    tipo = "VALOR"
                elif palabra.lower() == "fondo":
                    tipo = "FONDO"
                elif palabra.lower() == "valores":
                    tipo = "VALORES"
                elif palabra.lower() == "evento":
                    tipo = "EVENTO"
                # Crear el token
                x = tkn(tipo, palabra, linea)
                list_tkn.append(x)
                palabra = ""
                estado = 0
                i -= 1
        elif estado == 2:
            # ESTADO 2 -> cadena
            if c == "\"":
                palabra = palabra + c
                x = tkn("CADENA", palabra, linea)
                list_tkn.append(x)
                palabra = ""
                estado = 0
            elif c == "\n":
                linea = linea + 1
                palabra = palabra + c
                estado = 2
            else:
                palabra = palabra + c
                estado = 2
        i = i + 1


def imprimir_lsts():
    for x in list_tkn:
        print(x.gettoken())


def html222():
    ####### Comienza html
    with open('tokens.html', 'w') as f:
        f.write("<!DOCTYPE html>\n"
                "<html>\n"
                "<head>\n"
                "<title>Lista de Tokens</title>\n"
                '<link rel="stylesheet" href="estilos.css">\n'
                "</head>\n"
                "<body>\n"
                '<div id="main-container">\n'
                "<h1>Lista de Tokens</h1>\n"
                "<p>Creado por: Gerhard Benjamin Ardon Valdez 202004796</p>\n"
                "<table>\n"
                "<thead>\n"
                "<tr>\n"
                "<th>Token</th><th>Lexema</th><th>Linea</th>\n"
                "</tr>\n"
                "</thead>\n")

        ####### IMPRIMIR LOS OBJETOS

        for x in list_tkn:
            f.write("<tr><td>" + str(x.gettoken()) + "</td><td>" + str(x.getlexema()) + "</td><td>" + str(
                x.getlinea()) + "</td>\n</tr>")

        f.write("</table>\n"

                "</div>\n"
                "</body>\n"
                "</html>")

    with open('errores.html', 'w') as f:
        f.write("<!DOCTYPE html>\n"
                "<html>\n"
                "<head>\n"
                "<title>Lista de Errores</title>\n"
                '<link rel="stylesheet" href="estilos.css">\n'
                "</head>\n"
                "<body>\n"
                '<div id="main-container">\n'
                "<h1>Lista de Errores</h1>\n"
                "<p>Creado por: Gerhard Benjamin Ardon Valdez 202004796</p>\n"
                "<table>\n"
                "<thead>\n"
                "<tr>\n"
                "<th>Tipo</th><th>Lexema</th><th>Linea</th>\n"
                "</tr>\n"
                "</thead>\n")

        ####### IMPRIMIR LOS OBJETOS

        for x in list_err:
            f.write("<tr><td>" "Sintactico" + "</td><td>" + str(x.getlexema()) + "</td><td>" + str(
                x.getlinea()) + "</td>\n</tr>")

        f.write("</table>\n"

                "</div>\n"
                "</body>\n"
                "</html>")