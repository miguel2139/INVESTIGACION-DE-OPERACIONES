# Simplex-method-by-BigM (TI-nspire CAS)


Ejemplo:

      min -3x1 + x2 + x3
      s.a
      
      x1 - 2x2 +  x3 <= 11
    -4x1 +  x2 + 2x3 >=  3
    -2x1 +       +x3 =   1
    
            x1,x2,x3 >=  0
            

       Ver ejemplo.png

cuenta con las siguientes funciones y variables

     corre(A,b,c,inq,tp)      :  Corre el metodo simplex BigM hasta conseguir resultado
     ctableu(A,b,c,inq,tp)    :  Construye el tableu
     esctab(a,pos,va)         :  escribe tableu 
     pivota(w,aplha,beta)     :  pivota matriz w
     pivotabase(a,vp)         :  pivota una matriz a en las filas del vector vp          
     resultados(at,posb,cposb,n,tp)  :  Escribe resultados a partir del tableu y posicion de variables basicas
     tableu                   :   Tableu resultante
     x                        :   Vector de resultados
