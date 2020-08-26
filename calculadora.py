from tkinter import *
from calculadora_obj import *
main=Tk()

#-- instanciar obj calculadora

calculadora=Calculadora()

def introNum(num):
	valorAMostrar.set(valorAMostrar.get()+num)	

def realizarOperacion(operacion):
	calculadora.operacion=operacion
	calculadora.operar(valorAMostrar.get())
	

def mostrarResultado():
	realizarOperacion(calculadora.operacion)
	result = calculadora.obtenerResultado()
	valorAMostrar.set(result)


#--- input numeros ----
frame=Frame(main)
frame.pack()
valorAMostrar=StringVar()

cuadroNumeros=Entry(frame,textvariable=valorAMostrar)
cuadroNumeros.grid(row=0,column=0,pady=10,padx=10,columnspan=4)
cuadroNumeros.config(bg="black", fg="#00FF04")

#--- Teclas ----

fteclasnumeros=Frame(main)
fteclasnumeros.pack()

# --- fila 1 ---
tecla7=Button(fteclasnumeros,text="7",width="3",command=lambda:introNum("7"))
tecla7.grid(row=1,column=0)

tecla8=Button(fteclasnumeros,text="8",width="3",command=lambda:introNum("8"))
tecla8.grid(row=1,column=1)

tecla9=Button(fteclasnumeros,text="9",width="3",command=lambda:introNum("9"))
tecla9.grid(row=1,column=2)

btnDividir=Button(fteclasnumeros,text="/",width="3",command=lambda:introNum("/") )
btnDividir.grid(row=1,column=3)

# --- fila 2 ---
tecla4=Button(fteclasnumeros,text="4",width="3",command=lambda:introNum("4"))
tecla4.grid(row=2,column=0)

tecla5=Button(fteclasnumeros,text="5",width="3",command=lambda:introNum("5"))
tecla5.grid(row=2,column=1)

tecla6=Button(fteclasnumeros,text="6",width="3",command=lambda:introNum("6"))
tecla6.grid(row=2,column=2)

btnMultiplicar=Button(fteclasnumeros,text="X",width="3",command=lambda:realizarOperacion(2) )
btnMultiplicar.grid(row=2,column=3)

# --- fila 3 ---
tecla1=Button(fteclasnumeros,text="1",width="3",command=lambda:introNum("1"))
tecla1.grid(row=3,column=0)

tecla2=Button(fteclasnumeros,text="2",width="3",command=lambda:introNum("2"))
tecla2.grid(row=3,column=1)

tecla3=Button(fteclasnumeros,text="3",width="3",command=lambda:introNum("3"))
tecla3.grid(row=3,column=2)

btnRestar=Button(fteclasnumeros,text="-",width="3",command=lambda:realizarOperacion(1) )
btnRestar.grid(row=3,column=3)

# --- fila 4 ---
tecla0=Button(fteclasnumeros,text="0",width="3",command=lambda:introNum("0"))
tecla0.grid(row=4,column=0)

btnComa=Button(fteclasnumeros,text=",",width="3",command=lambda:introNum(","))
btnComa.grid(row=4,column=1)

btnIgual=Button(fteclasnumeros,text="=",width="3",command=lambda:mostrarResultado())
btnIgual.grid(row=4,column=2)

btnSumar=Button(fteclasnumeros,text="+",width="3",command=lambda:realizarOperacion(0))
btnSumar.grid(row=4,column=3)

main.mainloop()

