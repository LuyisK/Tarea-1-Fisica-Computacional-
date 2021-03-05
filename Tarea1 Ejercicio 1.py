# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 19:40:57 2021

@author: valec
"""
# Se definen las funciones de rapidez, que será la función a integrar; y la función de desplazamiento teórico, que determina el desplazamiento del vehículo en estudio. 

def Rapidez(v0, t0, v1, t1):
    return lambda ti: v0 + ti*(v1-v0)/(t1-t0)

def Desplazamiento_Teórico(v0, t0, v1, t1):
    return lambda ti: v0*ti + (ti**2)*(v1-v0)/(2*(t1-t0))

# Se define la función que permite obtener la aproximación del desplazamiento del automóvil con el método de Simspon 1/3 Compuesto.
 
def SimpsonUnTercio_Compuesta(a, b, n):
    aproximación = 0
    sumatoria = 0
    h = (b-a)/n

    for i in range(n):
         ti = a + (i*h)
         función = Rapidez(0.5, 0, 1, 100)
         func = función(ti)
         if ti == a or ti == b:
             sumatoria += func 
         elif i % 2 != 0:
             func = 4*func
             sumatoria += func
         elif i % 2 == 0:
             func = 2*func
             sumatoria += func
    
    aproximación = (h/3)*sumatoria
    
    return aproximación

print ("El desplazamiento del automóvil es:", SimpsonUnTercio_Compuesta(0, 100, 100000))

# Se crea una función que permite obtener la incertidumbre de la aproximación experimental con respecto al valor teórico del desplazamiento. 

def Porcentaje_Error():
    valor_teórico = Desplazamiento_Teórico(0.5, 0, 1, 100)(100)
    valor_experimental = SimpsonUnTercio_Compuesta(0, 100, 100000)
    porcentaje = ((abs(valor_teórico-valor_experimental))/valor_teórico)*100
    return porcentaje
                    
print ("El porcentaje de error es:", Porcentaje_Error(),"%")
