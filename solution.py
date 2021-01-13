import math 

f = open ("a_example","r")
Reader =f.read()
f.close()
print(Reader)

pizza=int(5)  #max number of pizza avilabel in this case 
Teams= ["1","2"] #This is for our understanding 
Total_members = int (5)
Total_ing =  int (7)

if(pizza != 5):
    print("sorry uh ! no Pizza left The stok is empty")


point =  Total_ing * Total_ing+Total_members* Total_members 


 
print("OUTPUT.........\n")
print("The pizza sent to ",Teams,"Member's groups  ")
print( " \n The number of ing sent to the teams")

print( "Total score is ",point)








