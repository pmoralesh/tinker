# Tkinter paso a paso

from tkinter import *
import time


ventana = Tk()   # instancio ventana a Tk
ventana.title("Esta es mi primera ventana")  # le doy un título a la ventana.

etiqueta = Label(ventana, text = "Hola Mundo en Python. Debo eliminar esta ventana  para que salga lasiguiente") # creo etiqueta a mostrar
etiqueta.pack()  # empaqueto la etiqueta dentro del frame ventana
boton = Button(ventana,text = "Minimizar", command = ventana.iconify)  #iconify minimiza la ventana.
boton.pack()





etiqueta.mainloop()  # La ventana queda esperando una acción.
                                       # no aparece el cursor en el idle

# Otro ejemplo
# ventana1

def parpadear():
    ventana1.iconify()  # minimizo ventana
    time.sleep(3)  # corro 3 segundos
    ventana1.deiconify()  # maximizo ventana.

ventana1 = Tk()
ventana1.title("Ventana de Eventos")  # le doy un título a la ventana.
etiqueta = Label(ventana1, text = "Ejemplo de Eventos.") # creo etiqueta a mostrar
etiqueta.pack()  # empaqueto la etiqueta dentro del frame ventana
etiqueta2 = Label(ventana1, text = "Debo de eliminar esta ventana  para que salga la siguiente") # creo etiqueta a mostrar
etiqueta2.pack()  # como se ha explicado, ubica la etiqueta.
boton = Button(ventana1, text = "Evento", command = parpadear) # command manda a ejecutar algo
boton.pack()  # ubico el botón con pack (una de las tres formas, falta grid y place)
ventana1.mainloop()  # activo la ventana1

# Ventana 2
# Botón salir

ventana3 = Tk()  # Instancio ventana3
def imprime():  # creo la función que command llamará
     print("Acabas de presionar imprimir")

ventana3.title("Tercera Ventana")
botonS = Button(ventana3, text = " Salir ", command = ventana3.destroy)
# en la línea anterior llamo al método Button y command es salir
botonS.pack()  # ubico
botonI = Button(ventana3, text = " Imprimir ", command = imprime)
botonI.pack()
etiqueta3 = Label(ventana3, text = "Ejemplo de Salir de la Ventana e imprimir") # creo etiqueta a mostrar
etiqueta3.pack()  # empaqueto la etiqueta dentro del frame ventana

ventana3.mainloop()

# Color, claro que sí.

ventana4 = Tk()  # Instancio ventana4
def imprime():  # creo la función que command llamará
     print("Acabas de presionar imprimir")

ventana4.title("Cuarta Ventana")
botonS = Button(ventana4, text = " Salir ", fg = 'red', command = ventana4.destroy)
# en la línea anterior llamo al método Button y command es salir
botonS.pack()  # ubico
botonI = Button(ventana4, text = " Imprimir ", fg = 'blue', command = imprime)
botonI.pack()
etiqueta4 = Label(ventana4, text = "Ejemplo de Botones con colores") # creo etiqueta a mostrar
etiqueta4.pack()  # empaqueto la etiqueta dentro del frame ventana

ventana4.mainloop()

# Ventana 5
# Ubicación de los botones izquierda y derecha

ventana5 = Tk()  # Instancio ventana4
def imprime():  # creo la función que command llamará
     print("Acabas de presionar imprimir")

ventana5.title("Quinta Ventana")
botonS = Button(ventana5, text = " Salir ", fg = 'red', command = ventana5.destroy)
# en la línea anterior llamo al método Button y command es salir
botonS.pack(side = LEFT)  # ubico
botonI = Button(ventana5, text = " Imprimir ", fg = 'blue', command = imprime)
botonI.pack(side = RIGHT)
etiqueta5 = Label(ventana5, text = "   Ejemplo de Botones Derecha e Izquierda   ") # creo etiqueta a mostrar
etiqueta5.pack()  # empaqueto la etiqueta dentro del frame ventana

ventana5.mainloop()


# Posicionamiento con Grid (Grilla)

ventana_grilla = Tk()
ventana_grilla.title("Posicionamiento mediante grilla")
boton = Button(ventana_grilla, text = 'Posicionamiento diferente r0, c1').grid(row = 0, column = 1)
boton = Button(ventana_grilla, text = 'Posicionamiento diferente r0, c0').grid(row = 0, column = 0)
boton = Button(ventana_grilla, text = 'Posicionamiento diferente r1, c1').grid(row = 1, column = 1)
boton = Button(ventana_grilla, text = 'Posicionamiento diferente r2, c1').grid(row = 2, column = 1)
ventana_grilla.mainloop()

# vPosicionamiento con Place

ventana_place = Tk()
ventana_place.title("Posicionamiento mediante place")
boton = Button(ventana_place, text = 'Posicionamiento diferente x10, y10').place(x=10, y = 10)
boton = Button(ventana_place, text = 'Posicionamiento diferente x220, y10').place(x=220, y = 10)
boton = Button(ventana_place, text = 'Posicionamiento diferente x10, y30').place(x=10, y = 30)
boton = Button(ventana_place, text = 'Posicionamiento diferente x220, y30').place(x=220, y = 30)
etiqueta_place = Label(ventana_place, text = "Ejemplo de posiconamiento con place")
etiqueta_place.place(x =120, y = 80)
ventana_place.mainloop()


# Ahora le damos tamaño a la ventana

ventana_place = Tk()
ventana_place.title("Posicionamiento mediante place y geometry")
ventana_place.geometry("435x200")  # Defino tamaño del frame o ventana.
boton = Button(ventana_place, text = 'Posicionamiento diferente x10, y10').place(x=10, y = 10)
boton = Button(ventana_place, text = 'Posicionamiento diferente x220, y10').place(x=220, y = 10)
boton = Button(ventana_place, text = 'Posicionamiento diferente x10, y30').place(x=10, y = 30)
boton = Button(ventana_place, text = 'Posicionamiento diferente x220, y30').place(x=220, y = 30)
etiqueta_place = Label(ventana_place, text = "Ejemplo de posiconamiento con place y geometry")
etiqueta_place.place(x =90, y = 80)
ventana_place.mainloop()

# Saludar con variables

def saludar():  # creo función saludar
    print("Hola: " + nombre.get() + "  " + apellidosP.get() + apellidosS.get() + " " + "de " + str(edad.get())
          + " años " + "y " + "sexo "+ str(sexo.get()) )

ventana = Tk()
ventana.geometry('400x220')
ventana.title("Entradas en Tkinter   ")
nombre = StringVar()  # declaro variable nombre como string.
apellidosP = StringVar()
apellidosS = StringVar()
edad = IntVar()
sexo = StringVar()

nombre.set("Escriba su nombre: ")  # set le da un valor por defecto a la variable nombre

etiqueta1 = Label(ventana, text = "Escriba su nombre: ").place(x=10,  y=10)
nombreCaja = Entry(ventana, textvariable = nombre).place(x=170, y=10) # defino dónde colocar la variable
etiqueta2 = Label(ventana, text = "Escriba su Apellido Paterno ").place(x=10,  y=40)
apellidosPCaja = Entry(ventana, textvariable = apellidosP).place(x=170, y=40) # defino dónde colocar la variable
etiqueta3 = Label(ventana, text = "Escriba su Apellido Materno ").place(x=10,  y=70)
apellidosSCaja = Entry(ventana, textvariable = apellidosS).place(x=170, y=70) # defino dónde colocar la variable
etiqueta4 = Label(ventana, text = "Edad ").place(x=10,  y=100)
edadCaja = Entry(ventana, textvariable = edad).place(x=170, y=100) # defino dónde colocar la variable
etiqueta5 = Label(ventana, text = "Sexo ").place(x=10,  y=130)
sexoCaja = Entry(ventana, textvariable = sexo).place(x=170, y=130) # defino dónde colocar la variable

boton = Button(ventana, text='Saludo Personalizado ', command = saludar).place(x=10, y = 170)

ventana.mainloop()
        

# Radiobutton

def operacion():
    numero = num.get()
    if opcion.get() == 1:
        print('Pasé por 1')
        total = numero * 10
    elif opcion.get() == 2:
        print('Pasé por 2')
        total = numero * 20
    elif opcion.get() == 3:
        print('Pasé por 3')
        total = numero * 30        
    elif opcion.get() == 4:
        print('Pasé por 4')
        total = numero * 40
    elif opcion.get() == 5:
        print('Pasé por 5')
        total = numero * 50
    elif opcion.get() == 6:
        print('Pasé por 6')
        total = numero * numero

    print("El total de la operación es: ", str(total))


ventana_radio = Tk()
ventana_radio.geometry('400x200')
ventana_radio.title("RadioButton en Tkinter")

opcion = IntVar()
num = IntVar()
num.set(9)  # le doy un valor a la cajNumero

etiqueta1 = Label(ventana_radio, text = "Escribe el número: ").place(x=20, y=20)
cajNumero = Entry(ventana_radio, textvariable = num).place(x=130, y=20)
etiqueta2 = Label(ventana_radio, text = "Escribe tu opción: ").place(x=20, y = 50)
# construyo el radiobutton
x10 = Radiobutton(ventana_radio, text = "X10", value = 1, variable = opcion).place(x=20, y=80)
x20 = Radiobutton(ventana_radio, text = "X20", value = 2, variable = opcion).place(x=70, y=80)
x30 = Radiobutton(ventana_radio, text = "X30", value = 3, variable = opcion).place(x=120, y=80)
x40 = Radiobutton(ventana_radio, text = "X40", value = 4, variable = opcion).place(x=20, y=110)
x50 = Radiobutton(ventana_radio, text = "X50", value = 5, variable = opcion).place(x=70, y=110)
cuadrado = Radiobutton(ventana_radio, text = "Cuadrado ", value= 6, variable = opcion).place(x=120, y=110)

boton = Button(ventana_radio, text = "Realza Operación", command = operacion).place(x=20, y=140)

ventana_radio.mainloop()


# SPINBOX

def obtener():
    print(valor.get())

ventana = Tk()
valor = StringVar()

ventana.title("Uso de Spinbox con Tkinter")
ventana.geometry('400x300')

etiqueta = Label(ventana, text = "Ejemplo 1 e Spinbox ").place(x=20, y = 20)
combo=Spinbox(ventana, values=("Uno","Dos","Tres","Cuatro","Cinco")).place(x=20, y = 50)
etiqueta2 = Label(ventana, text = "Ejemplo 2 de Spinbox").place(x = 20, y=80)
combo2=Spinbox(ventana, from_ = 1, to = 10, textvariable = valor).place(x=20, y = 110)
boton = Button(ventana, text = "Obtener valor Spinbox ", command = obtener).place(x=80, y=140)
ventana.mainloop()


# MessageBox

from tkinter import messagebox   # Importo la librería de los mensajes

def obtener():
    messagebox.showinfo('Mensaje', 'Tú, seleccionaste: ' + valor.get()) # Notar la coma, separa el
    # título y el texto del messagebox

ventana = Tk()
valor = StringVar()  # declaro valor como string
ventana.title("Uso de Spinbox con messagebox")
ventana.geometry('400x250')

etiqueta = Label(ventana, text = "Ejemplo 1 e Spinbox ").place(x=20, y = 20)
combo=Spinbox(ventana, values=("Uno","Dos","Tres","Cuatro","Cinco")).place(x=20, y = 50)
etiqueta2 = Label(ventana, text = "Ejemplo 2 de Spinbox").place(x = 20, y=80)
combo2=Spinbox(ventana, from_ = 1, to = 10, textvariable = valor).place(x=20, y = 110)
boton = Button(ventana, text = "Obtener valor Spinbox ", command = obtener).place(x=80, y=140)
# en la línea anterior el command llama a la función obtener que activa el messagebox
ventana.mainloop()

# Messagebox directo

from tkinter import messagebox

messagebox.showinfo("Hola", "Prueba directa de MessageBox")


# Messagebox Advertencia

from tkinter import messagebox

messagebox.showwarning("Advertencia", "Prueba directa de messabox de precaución")


# Messagebox Pregunta

from tkinter import messagebox

messagebox.askquestion("Pregunta 1", "¿Qué le pareció?")    

# Messagebox Pregunta Cancelar o no

from tkinter import messagebox

messagebox.askokcancel("Pregunta 2", "¿Cancela?")

# Messagebox Pregunta Sí  o no

from tkinter import messagebox

messagebox.askyesno("Pregunta 3", "¿Si o No?")

# Messagebox Reintentar

from tkinter import messagebox

messagebox.askretrycancel("Pregunta 4", "¿Quiere Reintentar?")



# Programa más completo:

from tkinter import messagebox

messagebox.showinfo("Atención ", "El programa a continuación es más complejo")

#######  Programa "Principal" por llamarlo así, ejemplo funcional.

# Programa agenda

from tkinter import *
from tkinter import messagebox

lista = []  # Creo una lista

# Función guardar

def guardar():  # función guardar
    n = nombre.get()  # n es igual a nombre de la Entry cajaN
    ap = apx.get() # Igual que la anterior, ap es el valor de la Entrey Apx
    am = apm.get() # la misma explicación
    c = correo.get()
    t = telefono.get()
    lista.append(n+"$"+ap+"$"+am+"$"+t+"$"+c)  # el dólar es para realizar el split más abajo
    escribirContacto()  # llamo a otra función
    messagebox.showinfo("guardo", "El contacto ha sido guardado en la agenda")
    nombre.set("")  # Reinicio a blanco el contenido de las varialbes, para no repetirlas
    apx.set("") # la misma explicación
    apm.set("")
    correo.set("")
    telefono.set("")
    consultar()  # llamo función consultar.

# Función eliminar

def eliminar():
    eliminado = conteliminar.get()  
    removido = False
    for elemento in lista:
        arreglo = elemento.split("$") # Separa los elementos de la lista por el valor $
        if conteliminar.get() == arreglo[3] : # índice 3 porque es el teléfono.
            lista.remove(elemento)  # Elimino el contacto de la lista.
            removido = True

        escribirContacto()  # Actualizo el archivo.
        '''
       El progtrama es muy bueno como ejemplo, pero la forma de trabajar no es funcional, cada vez que añado
       o elimino un elemtno a la lista el archivo "ag.txt" es creado y la informacón añadida nuevamente.
       Esto no es lo adecuado en un ambiente de trabajo.
        '''
        consultar()
        
        if removido:  # si removido = True, muestro el mensaje a continuacón.
            messagebox.showinfo("Eliminar","Elemento eliminado " + eliminado)

# Función consultar

def consultar(): # Muestra los elementos añadidos a la lista o los que quedan.

    # r es una ventana de texto, aparece en blanco en el frame.
    # ahí se muestra la información añadida.
    
    r = Text(ventana, width=80, height = 15)  # ventana es el frame
    lista.sort() # ordeno la lista
    valores = [] # creo lista valores
    r.insert(INSERT, "Nombre\tApèllidos P\t\tApellido M\t\tTeléfono\t\tCorreo\n")

    for elemento in lista:
        
        arreglo = elemento.split("$")  # split para separar los elementos por símbolo $ como separador
        valores.append(arreglo[3])  # añade al valores el campo teléfoo
        r.insert(INSERT, arreglo[0]+"\t" + arreglo[1] +"\t\t" + arreglo[2]  +"\t\t" +  arreglo[3]  +"\t\t" + arreglo[4]  +"\t\n")
        # la línea anterior es para insertar en el recuadro blanco "r" los valores de arreglo.
    r.place(x = 20, y = 230)
    spinTelefono = Spinbox(ventana, value=(valores), textvariable=conteliminar).place(x=450,y = 50)

    if lista == []:
        spinTelefono = Spinbox(ventana, value=(valores),textvariable=conteliminar).place(x=450, y = 50)
    r.config(state=DISABLED)   # si la lsita está vacía, la ventana r (la blanca del recuadro) se desactiva.
    
#   Función Iniciar Archivo

def iniciarArchivo():
    archivo = open("ag.txt","a")  # abro archivo .txt
    archivo.close()

# función cargar arhivo

def cargar():
    archivo = open("ag.txt", "r")
    linea = archivo.readline()  # Variabel linea cargo el contenido de readline

    if linea:  # si la lista "linea" tiene contenido
        while linea:  # mientras haya contenido en linea
            if linea[-1] =='\n':  # si el último elemtno es salto de linea
                linea = linea[:-1]  # -1 es el valor del último elemtno de la lista
            lista.append(linea)  # introduzco en la lista (lista) el valor de linea
            linea = archivo.readline() # vuelvo a leer otr línea del archvio.
            
        archivo.close  # cierro el archivo.
 
# función escribir contacto

def escribirContacto():
    archivo = open("ag.txt","w")  # abro el archivo para escritura.
    lista.sort() # ordeno la lista.

    for elemento in lista:
        archivo.write(elemento + "\n")   # grabo la información con un salto de linea
        
    archivo.close()

 # Definiciones:

ventana = Tk()  # Instancio la venta.
ventana.wm_attributes("-topmost", 1)  # Deja la ventana siempre arriba.

#########
# Declaro Variables
#########
nombre = StringVar()
apx = StringVar()
apm = StringVar()
correo = StringVar()
telefono = StringVar()
conteliminar = StringVar()
colorFondo = "#006"  # asigno el color a una variable
colorLetra = "#FFF"  # asigno el color a una variable

# LLamar funciones
iniciarArchivo()  # llamo al la función iniciar archivo
cargar()  # llamo función cargar
consultar() # llamo funcion

#########
# Configuro la ventana
#########
ventana.title("Agenda con archivos")
ventana.geometry("700x500")
ventana.configure(background = colorFondo)

etiquetaTitulo = Label(ventana, text = "Agenda con Archivos",
                        bg = colorFondo, fg = colorLetra).place(x=270, y=10)  # configuro etiqueta

etiquetaN = Label(ventana, text = "Nombre", bg = colorFondo,
                   fg = colorLetra).place(x = 50, y = 50) # Etiqueta dónde muestro Nombre
cajaN = Entry(ventana, textvariable = nombre).place(x=150, y = 50)  # aquí guardo el valor de nombre

etiquetaApx = Label(ventana, text = "Apellido Paterno", bg = colorFondo,
                    fg = colorLetra).place(x=50, y = 80)
cajaApx = Entry(ventana, textvariable = apx).place(x = 150, y = 80)

etiquetaApm = Label(ventana, text = "Apellido Materno", bg = colorFondo,
                    fg = colorLetra).place(x=50, y = 110)
cajaApm = Entry(ventana, textvariable = apm).place(x = 150, y = 110)

etiquetaT = Label(ventana, text = "Teléfono", bg = colorFondo,
                     fg = colorLetra).place(x=50, y = 140)
cajaT = Entry(ventana, textvariable = telefono).place(x = 150, y = 140)
 
etiquetaC = Label(ventana, text = "TCorreo", bg = colorFondo,
                     fg = colorLetra).place(x=50, y = 170)
cajaC = Entry(ventana, textvariable = correo).place(x = 150, y = 170)

etiquetaEliminar = Label(ventana, text = "Teléfono: ", bg = colorFondo,
                         fg = colorLetra).place(x = 370, y = 50)

spinTelefono = Spinbox(ventana, textvariable= conteliminar).place(x=450, y = 50)

botonGuardar = Button(ventana, text = "Guardar", command = guardar, bg = "#009",
                      fg = "white").place(x = 180, y = 200)

botonEliminar = Button(ventana, text = "Eliminar", command = eliminar, bg= "#009",
                      fg = "white").place(x=490, y = 80)

mainloop() # activo la ventana.

'''
La primera funcion llamada es "iniciararchivo()".  Esta función me crea el archvio ag.txt
Inmediatamente después llamo a la función "cargar()", la cual abre y lee el archivo para lectura.
La fución "consultar()" me muestra en una ventana llamada "r", la balcna grande, los valores
añadidos.

Después tenemos a los botones guardar (que llma a la función guadar()"
y el botón eliminar, que llama a la función eliminar().


'''
