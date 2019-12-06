import re
def factorial(x):
  global z
  z=1
  x=int(x)
  if x==0:
    z=1
  else:
    for y in range (0,x):
      z=z*(y+1)
  return z

def EvenOdd(x):
  global m
  x=str(x)
  if x[-1]==0:
    m=1
  elif x[-1]==2:
    m=1
  elif x[-1]==4:
    m=1
  elif x[-1]==6:
    m=1
  elif x[-1]==8:
    m=1
  else:
    m=2
  x=int(x)

def NchooseK(r, t):
  g=factorial(r)
  u=factorial(t)
  o=factorial(r-t)
  p=u*o
  d=g/p
  return d


def PascalTriangleLayer(placeholder):
  lays=[]
  for placeholder_ in range (placeholder+1):
    lays.append(NchooseK(placeholder, placeholder_))
  return(lays)



x=input("please input the first coefficient number of your binomial dont forget negatives I will assume that the variable is behind this number")
y=input("please input the second coefficient number of your binomial dont forget negatives I will assume that this coefficient has no variable")
e=input("please input the exponent that your binomial is multiplied by")
e=int(e)

m=""
for x in range (e+1):
  but=str(NchooseK(e, x))
  de=str(e-x)
  m+=but+"x^"+de
  if x!=e:
    m+="+"

print(m)
