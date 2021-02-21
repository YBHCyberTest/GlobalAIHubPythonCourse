import math
info={}
# listler oluşturmak :
StudentNames=["Yaser Bin Humidah","Ali Babu ","Yosuf Abraham","Mohammed Baby","Aisha Sofia"]
StudentGrades=[[25,50,20],[19,40,13],[8,46,25],[10,30,6,],[15,29,12]]
#öğrencilerin ismlerini ve puamlarını Toplayıp sözüğe aktarmak:
for name in StudentNames:
    for grade in StudentGrades:
         info[name]=(sum(grade))
         StudentGrades.remove(grade)
         break   
#öğrencilerin Toplam puanlarıyla sıralayıp göstirmek ve 
for i in sorted(info):
     print(f"Öğrencinin ismi :{i} Toplam Puanı => {info[i]}")
print("========================================================")
#Başarlı Olan Öğrenciler sıralayıp Tabrik etmek :  
for name,grade in info.items():
    if(grade >= 88):
        print(f"{name} ,Toplam Puanuuz =>{grade} , Mükemmel Tebrikler Başarlısnız")
    elif(grade >= 80 and grade <= 87):
        print(f"{name} , Puanuuz =>{grade} , Çok iyi Tebrikler Başarlısnız")
    elif(grade >= 73 and grade <= 79):
         print(f"{name} ,Toplam Puanuuz =>{grade} , iyi Tebrikler Başarlısnız")
    elif(grade >= 66 and grade <= 72):
        print(f"{name} ,Toplam Puanuuz =>{grade} , Orta Tebrikler Başarlısnız")  
    elif(grade >= 55 and grade <= 60):
        print(f"{name} ,Toplam Puanuuz =>{grade} , Yeterli  Başarlısnız")
    elif(grade >=55 and grade <= 59):
        print(f"{name} ,Toplam Puanuuz =>{grade} , Zayıf Geçtiniz")
    elif(grade >= 50 and grade <= 54): 
         print("{name} ,Toplam Puanuuz =>{grade} , Çok zayıf Gectiniz")
    else:
        print(f"{name} ,Toplam Puanuuz =>{grade} , Kötü Başarsızsınız")
             

             

    

    

   




    


    


   
    


  




        
        