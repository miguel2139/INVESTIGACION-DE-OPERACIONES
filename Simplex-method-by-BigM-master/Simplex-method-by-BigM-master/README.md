# Simplex-method-by-BigM
Motor de optimizacion realizado con python, que utiliza la metodologia BigM para resolver por operaciones de algebra lineal, 
esta libreria no utiliza numpy, solo las rutinas simples de python.

# Simplex-method-by-BigM-
V4.0
----
Esta version añadio en la evaluacion de las filas del pivote, la preferencia de quitar las variables slack de las base antes que otras. esto sucede cuando los valores son iguales y se tiene que definir que variable sacar de la base. se cambio la definicion de ineq, -1 = "<=" y 1 =">=", mas natural.

V3.0
----
Esta version agrega la evaluacion del resultado, para problemas infactibles (var slacks < Big M) o no acotadas (variables slack > 0)

     verificaerror(A,M,var) : funcion devuelve 1 o 0 si encuentra infactibilidad o no acotado.
     
Se incluyeron problemas tipos en archivo corre.py

V2.0
----
Esta version culmina la solucion incluyendo resultados y precio sombra de cada una de las restricciones

     resultados(A,bas,n,pos,pr)  : se ingresa tableu(A), listado de variables basicas(bas), numero de variables(n), posicion inicial de      bases(pos), tipo de problema('min' o 'max')

V1.0
----
Esta version añade rutinas de inversion de matrices y resolucion de ecuaciones.

    inv_matriz(A) : entrega como resultado matriz invertida

    res_ecuaciones(A,b) : entrega como resulado un vector de solucion de ecuaciones

<<<<<<< HEAD
>>>>>>> 351e883aae41a15b0dc0f4c909e2fc3f4b8884aa
=======
>>>>>>> 2c9142b2037228b817bbe6cc6211ad149154b82f
>>>>>>> version3

V0.0
----
Optimizacion mediante el metodo SIMPLEX, version general utilizando BigM


Ejemplo:

      min -3x1 + x2 + x3
      s.a
      
      x1 - 2x2 +  x3 <= 11
    -4x1 +  x2 + 2x3 >=  3
    -2x1 +       +x3 =   1
    
            x1,x2,x3 >=  0
            

<<<<<<< HEAD
  Para correr

     \>corre_simplex([[1,-2,1],[-4,1,2],[-2,0,1]],[-3,1,1],[11,3,1],[1,-1,0],'min')
     \>corre_simplex(A,b,c,ine,prob)
=======
     Para correr:  corre_simplex(A,b,c,inecuaciones,problema)
     valores para inecuaciones :
      -1 : '<='
       1 : '>='
       0 : '='
     
     valores para problema :
       'max'
       'min'

     \>corre_simplex([[1,-2,1],[-4,1,2],[-2,0,1]],[-3,1,1],[11,3,1],[1,-1,0],'min')
     
     
<<<<<<< HEAD
>>>>>>> 351e883aae41a15b0dc0f4c909e2fc3f4b8884aa
=======
>>>>>>> 2c9142b2037228b817bbe6cc6211ad149154b82f
>>>>>>> version3
  
