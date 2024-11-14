from tools import *
#ejemplos BigM
# min(max) cx
# s.a.
# ax (inq) b     inq: 1:'<=', -1:'>=', 0:'='
# x >= 0

f=0  #para impresion full

print('\nEjemplo 1\n---------')
c = [ -2,  3 ]
A = [[1 ,4], [2, 3],[ 2, 1]]
b = [4, 6 ,4]
inq = [-1, -1, -1]
corre_simplex(A,b,c,inq,'max',f)


print('\nEjemplo 2\n---------')
c=[-3,1,1]
b=[11,3,1]
A=[[1, -2, 1],[-4, 1, 2],[-2, 0, 1]]
inq=[-1, 1, 0]
corre_simplex(A,b,c,inq,'min',f)

print('\nEjemplo 3\n---------')
c = [1, 2, 3]
A = [[0, 1, 2], [3, 2, 1]]
b = [3, 6]
inq = [0, 0]
corre_simplex(A,b,c,inq,'min',f)

print('\nEjemplo 4\n---------') #aqui se puede observar que s1 <= -M, es infactible
c = [1,2]
A = [[1, 1] , [3, 2]]
b = [4, 6]
inq = [1, -1]
corre_simplex(A,b,c,inq,'max',f)

print('\nEjemplo 5\n---------')  #sin limites s1 es positivo todavia
c = [-1, -2]
A = [[1, 1], [1, -1]]
b = [3,1]
inq = [1,1]
corre_simplex(A,b,c,inq,'min',f)

print('\nEjemplo 6\n---------') # s1,s2,s3 <= -M,es infactible
c = [ 1, 1, 1, 1 ]
A = [ [1, 2, 0 ,1],[0, 0, 1, 3],[ 1, 0, 1, 0] ]
b = [2, 3, 6 ]
inq = [ -1, -1, 1 ]
corre_simplex(A,b,c,inq,'max',f)


print('\nEjemplo 7\n---------')  #sin limites s3 > 0
c = [ 1, 2, 3, 4 ]
A = [ [1, 2, -1, 2],[ 2, 0, 3, -1] ]
b = [ 4, 6 ]
inq = [ 1, 0 ]
corre_simplex(A,b,c,inq,'max',f)

print('\nEjemplo 8\n---------')  #sin limites s3 > 0
c = [-1,2,-3]
A = [ [1,1,1],[-1,1,2],[ 0, 2, 3],[0,0,1] ]
b = [ 6,4,10,2 ]
inq = [ 0,0,0,-1]
corre_simplex(A,b,c,inq,'min',f)
