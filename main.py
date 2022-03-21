import sys
import webbrowser
from tkinter import filedialog as fd
from tkinter import Tk
from main2 import *
from main3 import *

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk

    py3 = False
except ImportError:
    import tkinter.ttk as ttk

    py3 = True


contenido="p"




def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1(root)
    #autosave_support.init(root, top)
    root.mainloop()


w = None


def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    # rt = root
    root = rt
    w = tk.Toplevel(root)
    top = Toplevel1(w)
    #autosave_support.init(w, top, *args, **kwargs)
    return (w, top)


def destroy_Toplevel1():
    global w
    w.destroy()
    w = None


class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.', background=_bgcolor)
        self.style.configure('.', foreground=_fgcolor)
        self.style.configure('.', font="TkDefaultFont")
        self.style.map('.', background=
        [('selected', _compcolor), ('active', _ana2color)])

        top.geometry("541x419+383+106")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(0, 0)
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")

        self.Canvas1 = tk.Canvas(top)
        self.Canvas1.place(x=-10, y=-10, height=463, width=593)
        self.Canvas1.configure(background="#ffffff")
        self.Canvas1.configure(borderwidth="2")
        self.Canvas1.configure(cursor="fleur")
        self.Canvas1.configure(insertbackground="black")
        self.Canvas1.configure(relief="ridge")

        self.Canvas1.configure(selectbackground="blue")

        self.Canvas1.configure(selectforeground="white")

        self.Label1 = tk.Label(self.Canvas1)

        self.Label1.place(x=120, y=20, height=47, width=371)

        self.Label1.configure(background="#ffffff")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {@HP Simplified Jpan} -size 24 -weight bold")
        self.Label1.configure(foreground="#004080")
        self.Label1.configure(text='''FORMULARIOS DINAMICOS''')

        self.Button1 = tk.Button(self.Canvas1)
        self.Button1.place(x=40, y=110, height=44, width=157)
        self.Button1.configure(activebackground="#000000")
        self.Button1.configure(activeforeground="white")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#ccccff")
        self.Button1.configure(command=lambda: cargar() and self.Scrolledtext1.insert(tk.INSERT,contenido))
        self.Button1.configure(cursor="fleur")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font="-family {@HP Simplified Jpan} -size 15")
        self.Button1.configure(foreground="#004080")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(relief="groove")
        self.Button1.configure(text='''Cargar Archivo''')

        self.Scrolledtext1 = ScrolledText(self.Canvas1)
        self.Scrolledtext1.place(x=40, y=200, height=175, width=295)
        self.Scrolledtext1.configure(background="white")
        self.Scrolledtext1.configure(font="TkTextFont")
        self.Scrolledtext1.configure(foreground="black")
        self.Scrolledtext1.configure(highlightbackground="#d9d9d9")
        self.Scrolledtext1.configure(highlightcolor="black")
        self.Scrolledtext1.configure(insertbackground="black")
        self.Scrolledtext1.configure(insertborderwidth="3")
        self.Scrolledtext1.configure(selectbackground="blue")
        self.Scrolledtext1.configure(selectforeground="white")
        self.Scrolledtext1.configure(wrap="none")



        self.TLabel1 = ttk.Label(self.Canvas1)
        self.TLabel1.place(x=40, y=170, height=29, width=185)
        self.TLabel1.configure(background="#ffffff")
        self.TLabel1.configure(foreground="#004080")
        self.TLabel1.configure(font="-family {@HP Simplified Jpan} -size 13")
        self.TLabel1.configure(relief="flat")
        self.TLabel1.configure(anchor='w')
        self.TLabel1.configure(justify='left')
        self.TLabel1.configure(text='''Modificar el codigo:''')

        self.Button2 = tk.Button(self.Canvas1)
        self.Button2.place(x=370, y=270, height=44, width=157)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#ccccff")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(font="-family {@HP Simplified Jpan} -size 15")
        self.Button2.configure(foreground="#004080")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(relief="groove")
        self.Button2.configure(text='''Analizar''')
        global contenido
        self.Button2.configure(command=lambda:   guardar(self.Scrolledtext1.get("1.0", tk.END)))


        self.Button3 = tk.Button(self.Canvas1)
        self.Button3.place(x=370, y=330, height=44, width=157)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#ccccff")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(font="-family {@HP Simplified Jpan} -size 15")
        self.Button3.configure(foreground="#004080")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(relief="groove")
        self.Button3.configure(text='''Reportes''')
        self.Button3.configure(command=lambda: webbrowser.open_new_tab('tokens.html') and webbrowser.open_new_tab('errores.html') and webbrowser.open_new_tab('pagina.html'))

        self.menubar = tk.Menu(top, font="TkMenuFont", bg=_bgcolor, fg=_fgcolor)
        top.configure(menu=self.menubar)

def cargar():
    ############### LEER EL ARCHIVO
    Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
    filename = fd.askopenfilename(title="Select file", filetypes=(("Form Files", "*.form"), ("ALL", "*.*")))
    print(filename)
    file = open(filename, encoding="utf8")
    global contenido
    contenido = file.read()
    ############## "contenido" es la variable que contiene toda la información leída
    return contenido

def guardar(x):
    global contenido
    contenido=x
    analizar(contenido)
    html222()
    try:
        formular(contenido)
        htmlformulario()
    except:
        print("")


# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''

    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))
        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')
        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)
        # Copy geometry methods of master  (taken from ScrolledText.py)
        if py3:
            methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() \
                      | tk.Place.__dict__.keys()
        else:
            methods = tk.Pack.__dict__.keys() + tk.Grid.__dict__.keys() \
                      + tk.Place.__dict__.keys()
        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''

        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)

        return wrapped

    def __str__(self):
        return str(self.master)


def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''

    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
        container.bind('<Leave>', lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)

    return wrapped


class ScrolledText(AutoScroll, tk.Text):
    '''A standard Tkinter Text widget with scrollbars that will
    automatically show/hide as needed.'''

    @_create_container
    def __init__(self, master, **kw):
        tk.Text.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)


import platform


def _bound_to_mousewheel(event, widget):
    child = widget.winfo_children()[0]
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-MouseWheel>', lambda e: _on_shiftmouse(e, child))
    else:
        child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))
        child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))


def _unbound_to_mousewheel(event, widget):
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        widget.unbind_all('<MouseWheel>')
        widget.unbind_all('<Shift-MouseWheel>')
    else:
        widget.unbind_all('<Button-4>')
        widget.unbind_all('<Button-5>')
        widget.unbind_all('<Shift-Button-4>')
        widget.unbind_all('<Shift-Button-5>')


def _on_mousewheel(event, widget):
    if platform.system() == 'Windows':
        widget.yview_scroll(-1 * int(event.delta / 120), 'units')
    elif platform.system() == 'Darwin':
        widget.yview_scroll(-1 * int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.yview_scroll(-1, 'units')
        elif event.num == 5:
            widget.yview_scroll(1, 'units')




def _on_shiftmouse(event, widget):
    if platform.system() == 'Windows':
        widget.xview_scroll(-1 * int(event.delta / 120), 'units')
    elif platform.system() == 'Darwin':
        widget.xview_scroll(-1 * int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.xview_scroll(-1, 'units')
        elif event.num == 5:
            widget.xview_scroll(1, 'units')




if __name__ == '__main__':
    vp_start_gui()
