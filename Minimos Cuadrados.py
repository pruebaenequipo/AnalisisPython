# -*- coding: utf-8 -*-
#Jhoan David Ramirez Grajales
###MINIMOS CUADRADOS###
import numpy as np
from matplotlib import pyplot

def sumatoriaCuadrado(x):
    sumatoria=float(0)
    for i in range(tamano):
        sumatoria+=x[i]**2
    return sumatoria

def sumatoriaDatos(x):
    sumatoria=float(0)
    for i in range(tamano):
        sumatoria+=x[i]
    return sumatoria

def sumatoriaProducto(x,y):
    sumatoria=float(0)
    for i in range(tamano):
        sumatoria+=x[i]*y[i]
    return sumatoria

def minimosCuadrados(x,y):
    global m, b
    m=(sumatoriaProducto(x,y)-sumatoriaDatos(x)*sumatoriaDatos(y)/tamano)/(sumatoriaCuadrado(x)-sumatoriaDatos(x)**2/tamano)
    b=(np.mean(y)-m*np.mean(x))
    print m
    print b
def f1(x):
    global m, b
    return m * x + b
    
def graficar():
    pyplot.plot(x,y,'o') #grafico los puntos en las coordenadas X,Y 
    rango=range(0,20)
    #grafico la recta que se ajusta a los datos en el rango de cero a 20
    pyplot.plot(rango,[f1(i) for i in rango])  
    # Establecer el color de los ejes.
    pyplot.axhline(0, color="black")
    pyplot.axvline(0, color="black")
    pyplot.show()

################################################
tamano=int(9)
m=float(0)
b=float(0)
x=[7,1,10,5,4,3,13,10,2]
y=[2,9,2,5,7,11,2,5,14]
minimosCuadrados(x,y)
graficar()



