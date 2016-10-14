import random
t1=input("enter team 1:")
b1=input("enter batsman name:")
i1=input("enter bowler name:")
t2=input("enter team 2:")
b2=input("enter batsman name:")
i2=input("enter bowler name:")
print(t1,"batting first")
sum1=0
for i in range(1,7):
         print(i2,"bowls ball",i)
         x=random.randrange(0,6)
         print(b1,"scores",x)
         sum1=sum1+x
print("scores o",t1,"=",sum1)
print(t2,"batting first")
sum2=0
for i in range(1,7):
         print(i2,"bowls ball",i)
         x=random.randrange(0,6)
         print(b2,"scores",x)
         sum2=sum2+x
print('score of',t2,"=",sum2)
if(sum1>sum2):
   print(t1,"is the winner")
elif(sum1==sum2):
    print("the match is draw")
else:print(t2,"is the winner")





         
         
