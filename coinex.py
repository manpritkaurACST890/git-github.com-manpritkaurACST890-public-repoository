#Coin tossing
#simulates a fair coin by writing 'Heads' and 'Tails', depending on the outcome of a random number generator.
import random      # import the random module
Heads=0            # total number of heads appearing (starting from 0)
Tails=0            # total number of tails apperaing (starting from 0)

for i in range(0,100):

   flip=random.randint(0,1)       # generating the random variables

   if flip==0 :
     Heads+=1                    # adding 1 everytime heads appear
   else:
     Tails+=1                    # adding 1 everytime tail appears
print("Heads count %i." %Heads)  # total head appered
print("Tails count %i." %Tails)  # total tail appeared