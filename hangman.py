import repl
import random
def enter():#my function
  print("")
wordys=["are", "red", "row", "war", "sew"]
randomword=random.choice(wordys)#choosing the word
stopper=6
length=len(randomword)
correct=0
guessed=""
print("_ "*length)
lastone="_ _ _"
while stopper>0:# my loop
  inyput=input("letter please")
  inyput=inyput.lower()#the input
  enter()
  print("you are playing hangman")
  enter()
  instring=inyput in randomword
  wasguess= inyput in guessed
  if wasguess==True:#determining whether yor guess is right wrong already said the input lost or won
    print("you already said that")
    guessed=guessed+inyput
    print("you have guessed "+guessed)
  elif instring==True:
    print("you were right")
    correct=correct+1
    print(correct)
    guessed=guessed+inyput
    print("you have guessed "+guessed)
  elif instring==False:
    print("you were wrong try again")
    stopper=stopper-1
    stopper=str(stopper)
    print("you now have "+stopper+" lives")
    stopper=int(stopper)
    guessed=guessed+inyput
    print("you have guessed "+guessed)
  elif stopper==0:
    print("you lost")
    print("the word was "+ randomword)
    guessed=guessed+inyput
    print("you have guessed "+guessed)
  if instring==True: #the letter display _ _ _
    if correct==0:
      correct0="_ "*length
      print=correct0
      lastone=correct0
    elif correct==1:
      correctinyput1=inyput
      place1=randomword.find(correctinyput1)
      afterplace=length-(place1+1)
      correct1="_ "*place1+correctinyput1+"_ "*afterplace
      print(correct1)
      lastone=correct1
    elif correct==2:
      correctinyput2=inyput
      place2=randomword.find(correctinyput2)
      afterplace2=length-(place2+1)
      if place2>place1:
        betweenplace21=place2-(place1+1)
        correct21="_ "*place1+correctinyput1+"_ "*betweenplace21+correctinyput2+"_ "*afterplace2
        print(correct21)
        lastone=correct21
      elif place1>place2:
        betweenplace12=place1-(place2+1)
        correct22="_ "*place2+correctinyput2+"_ "*betweenplace12+correctinyput1+"_ "*afterplace
        print(correct22)
        lastone=correct22
    elif correct==3:
      print(randomword)
  elif instring==False:# still the display this time if your letter is not correct
    print(lastone)
  if length==correct:
    stopper=0
    print("you win")
    guessed=guessed+inyput
    print("you have guessed "+guessed)
    
print(randomword)
