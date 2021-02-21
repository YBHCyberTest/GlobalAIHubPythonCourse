import random
list1=[]
row=3
cols=3
marix=[]
for i in range (0,1000):
    bolundu = False
    for j in range(2,i):
            if i % j == 0:
                bolundu=True
                # break yok...
    if bolundu == False:
        list1.append(i)
##############################################
for i in range(row):   
    marix.append(random.sample(list1,9))
print("3*3 matrix with 9 random prime numbers is :")

for a in range(row):
    for b in range(cols):
        print(marix[a][b],end=" ")      
    print()


    


    

