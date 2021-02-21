def  prime_first(i):
    if(i<500):
         bolundu = False
         for j in range(2,i):
             if i % j == 0:
                bolundu=True
         if bolundu == False:
            print(i)         
######################################### 
def  prime_second(i):
    if(i>=500):
         bolundu = False
         for j in range(2,i):
             if i % j == 0:
                bolundu=True
         if bolundu == False:
            print(i)   
######################################### 
for i in range(0,1000):
    prime_first(i)
    if(i==500):
        print("=========================")
    prime_second(i)

   
    
   
        




             
    
            
                
    

   