import repl
put=input("please enter a roman numeral under 100")
puty=put.upper()
leng=len(puty)
a=0
b=0
c=0
d=0
e=0
f=0
g=0
h=0
letters=[a, b, c, d, e, f, g, h]
x=0
def LetToNumb(x):
  for y in range(0,x):
    if puty[y]=="I":
      letters[y]=1
    elif puty[y]=="V":
      letters[y]=5
    elif puty[y]=="X":
      letters[y]=10
    elif puty[y]=="L":
      letters[y]=50
    elif puty[y]=="C":
       letters[y]=100
for l in range(0,8):
  if leng==l:
    LetToNumb(l)
if letters[0]<letters[1]:
  letters[0]=-letters[0]
if letters[1]<letters[2]:
  letters[1]=-letters[1]
if letters[2]<letters[3]:
  letters[2]=-letters[2]
if letters[3]<letters[4]:
  letters[3]=-letters[3]
if letters[4]<letters[5]:
  letters[4]=-letters[4]
if letters[5]<letters[6]:
  letters[5]=-letters[5]
if letters[6]<letters[7]:
  letters[6]=-letters[6]
summy=sum(letters)
print(summy)
