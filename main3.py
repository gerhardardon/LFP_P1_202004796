import re

list_comp = []
html = ""


class comp:
    def __init__(self, tipo="-", valor="-", fondo="-", valores="-", evento="-", nombre="-"):
        self.tipo = tipo
        self.valor = valor
        self.fondo = fondo
        self.valores = valores
        self.evento = evento
        self.nombre = nombre
        pass

    def getinfo(self):
        print("____________________")
        print("TIPO:", self.tipo)
        print("VALOR:", self.valor)
        print("FONDO:", self.fondo)
        print("VALORES:", self.valores)
        print("EVENTO:", self.evento)
        print("NOMBRE:", self.nombre)

    def html_comp(self):
        global html
        if self.tipo == "etiqueta":
            return '<br><label>' + self.valor + '</label>'
        elif self.tipo == "texto":
            return '<br><input type="text" value="' + self.valor + '"placeholder="' + self.fondo + '"/>'
        elif self.tipo == 'grupooption':
            html = "<br>"
            html += '''<select>
            <optgroup label="''' + self.nombre + '''">
            <option>''' + self.valores + '''</option>
            </optgroup>

  </select>'''
            return html
        elif self.tipo == "gruporadio":
            html = "<br>"
            html += '''<label> ''' + self.nombre + '''
            <input type="radio" name="''' + self.nombre + '''" value="''' + self.valores + '''">''' + self.valores + '''
            </label>'''
            return html

        elif self.tipo == "boton":
            html = "<br>"
            html = '''<style>
    .button {
      border: none;
      color: white;
      padding: 15px 32px;
      text-align: center;
      text-decoration: none;
      display: inline-block;
      font-size: 16px;
      margin: 4px 2px;
      cursor: pointer;
    }

    .button1 {background-color: #4CAF50;} /* Green */
    .button2 {background-color: #008CBA;} /* Blue */
    </style>

            '''
            if self.evento == "entrada":
                html += '''
                   <br> <button class="button button1">''' + "self.evento" + '''</button>'''
            else:
                html += '''<br><button class="button button2">Blue</button>'''

            return html


def formular(contenido):
    global list_comp

    palabra = ""
    tipe = ""
    estado = -1

    for x in contenido:
        if estado == -1:
            if x == "<":
                componente = comp()
                print(x)
                estado = 0
            if x == '\"':
                estado = 1
                continue

        if estado == 0:
            if re.search("[a-zA-Z]", x):
                tipe += x
            if x == ":":
                tipe.replace(" ", "")
                print(tipe)
                estado = -1
            if x == ">":

                print(x)
                try:
                    list_comp.append(componente)
                except:
                    print("")
                estado = -1
        if estado == 1:
            if re.search("[a-zA-Z]", x):
                palabra += x
            if x == '\"':
                palabra.strip()
                if tipe.lower() == "tipo":
                    componente.tipo = palabra
                elif tipe.lower() == "valor":
                    componente.valor = palabra
                elif tipe.lower() == "fondo":
                    componente.fondo = palabra
                elif tipe.lower() == "valores":
                    componente.valores = palabra
                elif tipe.lower() == "evento":
                    componente.evento = palabra
                elif tipe.lower() == "nombre":
                    componente.nombre = palabra

                tipe = ""
                palabra = ""
                estado = 0


def htmlformulario():
    ####### Comienza html
    with open('pagina.html', 'w') as f:
        f.write("<!DOCTYPE html>\n"
                "<html>\n"
                "<head>\n"
                "<title>form</title>\n"

                "</head>\n"
                "<body>\n"
                '<div id="main-container">\n'
                "<h1>Form</h1>\n"
                "<p>Creado por: Gerhard Benjamin Ardon Valdez 202004796</p>\n")

        for x in list_comp:
            f.write(x.html_comp())

        f.write("</div>\n"
                "</body>\n"
                "</html>")

    global html
    html = ""
