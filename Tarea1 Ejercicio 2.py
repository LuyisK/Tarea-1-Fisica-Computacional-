# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 23:13:45 2021

@author: valec
"""
# Se inmporta la biblioteca de numpy para el cálculo del valor teórico del problema.

import numpy as np

# Se definen como funciones anónimas el desplazamiento y la derivada de este. 

f = lambda y: -5 + (1/2)*0.01*y**2 
df = lambda y: 0.01*y

# Se crea la función para obtener una aproximación del tiempo con el método de derivación numérica de Newton Raphson. 

def Newton_Raphson(fx, dfx, xi, tol):
    t = xi
    n = 1
    error = 1
    while error > tol:
        ti = t -fx(t)/dfx(t)
        error = abs(t-ti)/abs(t)
        t = ti
        n += 1
    print("Solución aproximada:", t)
    print("Error relativo normalizado: ",error)
    print("Número de iteraciones:", n)

Newton_Raphson(f, df, 1, 0.01)    

# La siguiente función calcula la incertidumbre con respecto al valor real del tiempo al cual el vahículo pasa por x = 0m.
 
def Porcentaje_Error():
    valor_teórico = np.sqrt(10/0.01)
    valor_experimental = 31.622782450701045 
    #Se debe ingresar el valor experimental obtenido a partir de la función anterior manualmente. 
    porcentaje = ((abs(valor_teórico-valor_experimental))/valor_teórico)*100
    return porcentaje 

print("El porcentaje de error con respecto al valor real es de: ", Porcentaje_Error())
    
    
    

