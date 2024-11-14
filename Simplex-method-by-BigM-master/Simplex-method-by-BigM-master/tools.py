import math, copy

#para mostrar los caracteres unicode
import io,sys
sys.stdout = io.open(sys.stdout.fileno(), 'w', encoding='utf8')
#print(sys.stdout.encoding)

def corre_simplex(A,b,c,ine,prob,fr): #Corre simplex llama a todas rutinas
    verproblema(A,b,c,ine,prob)
    M=100
    (A,var,bas,pos)=tableu(A,b,c, ine, prob,M) # M al final
    if fr :  #fr flag reporte para emitir todos los tableu y proceso
     print('Tableu inicial')
     vertableu(A,bas,var)
    A=pivotabase(A,pos)
    if fr:
     print('Tableu')
     vertableu(A,bas,var)
    #print('variables=',var)
     print('var.basicas=',bas)
     print('indice basicas',pos)
     print('----SIMPLEX----')
    for k in range(0,10):
      index=indexpivote(A,bas,var)
      if index[0] > -1 and index[1] > -1:
        A=pivot(A,index)
        bas[index[0]-1]=var[index[1]-1]
        if fr:
         print('paso',k+1,': pivote encontrado=',index, sep='')
         vertableu(A,bas,var)
    if verificaerror(A,M,var) == 0:
        print('Solucion :')
        resultados(A,bas,len(c),pos,prob)
    else :
        vertableu(A,bas,var)

def verproblema(AA,bb,cc,ine,prob):
	A=copy.deepcopy(AA)
	b=copy.deepcopy(bb)
	c=copy.deepcopy(cc)
	n = len(c)
	m = len(b)
	# funcion objetivo
	print(prob,' ',end='',sep='')
	for i in range(n):
		t= c[i]
		if i > 0 :
			if t < 0:
				t=-1*t
				print(' - ',end='')
			else :
			    print(' + ',end='')
		elif t == -1:
			t=-1*t
			print('-',end='')
		if t == 1 :
			print(f'x{i+1}',end='')
		else:
			print(f'{t}x{i+1}',end='')

	#restricciones
	print('\n','s.a.:',sep='',end='')

	for i in range(m):
		print('\n  ',end='')
		for j in range(n):
			t = A[i][j]
			if t == 0 :
				print('   ',end='')
			else:
				if j > 0 :
					if t < 0:
						t=-1*t
						print(' - ',end='')
					else :
						print(' + ',end='')
				elif t == -1:
					t=-1*t
					print('-',end='')
				if t == 1 :
					print(f'x{j+1}',end='')
				else:
					print(f'{t}x{j+1}',end='')
		if ine[i] == 1:
			print(' \u2265',b[i],end='')
		elif ine[i] == -1:
			print(' \u2264',b[i],end='')
		elif ine[i] == 0:
			print(' =',b[i],end='')
	#variables >= 0
	print('\n\n  ',end='')
	for i in range(n):
		print(f'x{i+1}',end='')
		if i < n-1 :
			print(',',end='')
	print(' \u2265 0\n')

def verificaerror(A,M,var):
    n=len(A[0])-1
    m=len(A)-1
    funb=0
    finf=0
    for j in range(n):  #se revisa solo entre las slack
       if var[j][0:1] == 's' and A[m][j]  > 0 :
           funb =1
       elif var[j][0:1] == 's' and A[m][j]  <= -M :
           finf=1
    if funb : print('Error : El problema no esta acotado')
    if finf : print('Error : El problema es infactible')
    return funb + finf

def tableu(AA,bb,cc, inq, pr, M):  #construye el tableu de los datos.
    A=copy.deepcopy(AA)
    b=copy.deepcopy(bb)
    c=copy.deepcopy(cc)
    ineqq=copy.deepcopy(inq)
    prob=copy.deepcopy(pr)

    #las listas de variables
    variables=[]
    base=[]
    posbase=[]
    n = len(c)
    m = len(A)

    #inicializacion de variables
    for j in range(n):  #c tiene la cantidad de variables
        variables.append(f"x{j+1}")
    c = [x*-1 for x in c]  #para minimizacion
    if prob == 'max' :
        c = copy.deepcopy(cc)
    A.append(c)   #añade al final
    b.append(0)
    zero=[0.0]*len(b)
    naux=0
    nslack=0

    #construccion de tableu
    for i in range(0,len(ineqq)):
      A=appendcol(A,zero)
      if ineqq[i] == 1:
          A[i][n+nslack+naux]=-1
          variables.append(f"s{nslack+1}")
          nslack +=1
          #bigM aux
          A=appendcol(A,zero)
          A[i][n+nslack+naux]=1
          variables.append(f"a{naux+1}")
          base.append(f"a{naux+1}")
          A[m][n+nslack+naux]=-M
          naux +=1
      elif ineqq[i] == 0:
          A[i][n+nslack+naux]=1
          variables.append(f"a{naux+1}")
          base.append(f"a{naux+1}")
          A[m][n+nslack+naux]=-M
          naux +=1
      elif ineqq[i] == -1:
          variables.append(f"s{nslack+1}")
          base.append(f"s{nslack+1}")
          A[i][n+nslack+naux]=1
          nslack +=1
      posbase.append(n+nslack+naux)
    return (appendcol(A,b),variables,base,posbase)

def pivot(A, pivot_index):		# pivota un index+1 en una matriz A
        ''' Perform operations on pivot.
        '''
        T=copy.deepcopy(A)
        i,j = pivot_index[0]-1,pivot_index[1]-1
        pivot = T[i][j]
        T[i] = [element / pivot for
                           element in T[i]]
        for index, row in enumerate(T):
           if index != i:
              row_scale = [y * T[index][j]
                          for y in T[i]]
              T[index] = [x - y for x,y in
                                     zip(T[index],
                                         row_scale)]
        return T

def pivotabase(T,V): #hace pivotes consecutivos basados en vector col
    A=copy.deepcopy(T)
    pos=copy.deepcopy(V)
    for k in range(0,len(pos)):
      A=pivot(A,[k+1,pos[k]])
    return A

def pivotec(vv,vari): #evaluacion de columnas simplex devuelve indexj
    v=copy.deepcopy(vv)
    vmax=-1
    jmax=-2
    temp=vmax
    for j in range(0,len(v)-1):
      temp=v[j]
      if vari[j][0:1] != 'x':
         temp  = temp - 0.00009
      if temp > 0 and temp > vmax:
      	vmax = v[j]
      	jmax = j
    return jmax

def pivotef(vv,bb,basi): #evaluacion de filas simplex devuelve indexi
	  v=copy.deepcopy(vv)
	  b=copy.deepcopy(bb)
	  vmin = 999999999.99
	  imin = -2
	  temp = vmin
	  for i in range(0,len(bb)-1):
	    if v[i] != 0 :
	       temp = b[i]/v[i]
	    if basi[i][0:1] == 's':
	       temp = temp - 0.009
	       #print(basi[i][0:1], temp)
	    if v[i] != 0 and temp > 0 and temp < vmin:
	  	    vmin = temp
	  	    imin = i
	  return imin

def indexpivote(AA,basi,vari): #llama al calculo de index
    A=copy.deepcopy(AA)

    indexj=pivotec(A[len(A)-1],vari)+1

    bb=vcol(A,len(A[0]))
    vv=vcol(A,indexj)
    indexi=pivotef(vv,bb,basi)+1
    return [indexi,indexj]

#herramientas auxiliares
def appendcol(T,vc): #añade el vector vc (columna) a matriz T
    A=copy.deepcopy(T)
    b=copy.deepcopy(vc)
    for i in range(0, len(A)):
      A[i] += [b[i]]  #añade al final de la suma
    return A

def vcol(A,cc):  #obtiene un vector (columna cc)  de matriz A
    c=copy.deepcopy(cc)
    c-=1
    v=[]
    #print(c)
    for i in range(0,len(A)):
    	v.append(A[i][c])
    return v

def ver(A): #muestra la matriz A en otro formato
	for k in A:
		for j in k:
		   val = redondea(j)
		   print('{0:7.1f}'.format(val),end='')
		print()

def vertableu(AA,vbase,vvar): #Muestra tableu
    A = copy.deepcopy(AA)
    var=copy.deepcopy(vvar)
    base = copy.deepcopy(vbase)
    base.append('z ')
    print('       ',end='')
    for i in var:
      print('{0:7}'.format(i),end='')
    print()
    for k in range(0,len(A)):
      print(base[k],end='')
      for j in range(0,len(A[k])):
        val = redondea(A[k][j])
        print('{0:7.1f}'.format(val),end='')
      print()

def redondea(x): #redondea para print a n decimales
	x = math.ceil(x*10000)/10000
	return x

def identidad(n): #crea matriz identidad de n elementos
	MI = [[1 if j == i else 0 for j in range(n)] for i in range(n)]
	return MI

def mzero(n):  #crea matriz cero de n elementos
    MI = [[0 for j in range(n)] for i in range(n)]
    return MI

#mas herramientas
def res_ecuaciones(AA,bb): #resuelve sistema de ecuaciones
    A=copy.deepcopy(AA)
    b=copy.deepcopy(bb)
    A=appendcol(A,b)
    n=len(A)
    bas=[]
    sol=[]
    for i in range(n):
        bas.append(i+1)
    A=pivotabase(A,bas)
    for i in range(n):
        sol.append(A[i][n])
        print('x',i+1,'=',A[i][n],sep='')
    return sol

def inv_matriz(AA): #invierte matriz
    A=copy.deepcopy(AA)
    n=len(A)
    I=identidad(n)
    sol=mzero(n)

    for i in range(n):
     A=appendcol(A,I[i])

    bas=[]
    for i in range(n): #basicas para pivotar
        bas.append(i+1)

    A=pivotabase(A,bas)
    sol = [[A[i][n+j] for j in range(n)] for i in range(n)]
    print('inv=')
    ver(sol)
    return sol

def resultados(A,bas,n,pos,pr): # muestra resultados finales
    variables =[]
    valor=[]
    m=len(bas)  #nro de restriccion o variables basicas
    mA=len(A[0])-1 #columna de RHS
    for k in range(n): #para todas las x
     variables.append(f"x{k+1}")
     valor.append(0)
     for i in range(m): #para todas las variables basicas
       if variables[k] == bas[i]:
           valor[k] = A[i][mA]
     print(variables[k],valor[k])
    print('z',redondea(A[m][mA])*(-1 if pr=='max' else 1))

    print('Duales:')
    for j in range(len(pos)):
      print(f'w{j+1}',redondea(A[m][pos[j]-1])*(-1 if pr=='max' else 1))
