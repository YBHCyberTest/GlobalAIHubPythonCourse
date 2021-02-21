
import random

class Game:
    
    #Initializer / Instance Attributes
    def __init__(self):
        
        self.flag = True
        
        print("...Welcome, let's play hangman...")
        print("\nThe rules are:\n\tEnter one character at a time.\n\tDebe ser una letra del alfabeto.\n\tIt must be a letter of the alphabet,1 attempt will be subtracted from you.")
        
        word_list = ["ant","baboon", "badger","bat", "bear", "beaver", "camel", "cat", "clam", "cobra", "cougar", "coyote", "crow", "deer", "dog","donkey" "duck","eagle", "ferret", "fox" "frog", "goat","goose","hawk","lion","lizard","llama","mole","monkey","moose","mule","newt","otter","owl","panda","parrot","pigeon","python","rabbit","ramrat","raven","rhino","salmon","seal","shark","sheep","skunk","sloth","snake","spider","stork","swan","tigertoad","trout","turkey","turtle","weasel","whale","wolf","wombat", "zebra'"]
       
        self.word_list = [item.lower() for item in word_list]#Poner todo a minúscula
        
        self.discovered = []
        
        self.attempt = 5
        
        return None
    
    #Instance method
    def random_word(self):
        
        word= random.choice(self.word_list)
        self.word=word
            
    
    #Instance method
    def init_asteriscos(self):
        
        lista=['*' for i in range(len(self.word))]
        print("\nThe word has {0} letters".format(len(self.word)))
        print(''.join(lista))
        self.lista=lista
        return None
    
    def life_counter_status(self):
        
        if (self.attempt)!=1:
            print("\nYou have {0} attempts".format(self.attempt))
        else:
            print("\nYou have {0} attempt".format(self.attempt))

        return self.attempt
    
    def letter(self):
        #Pedir la letra
        letra=str(input("Write the word : "))
        letra=letra.lower() #Pasarla a minuscula por cualquier cosa
        self.letra=letra
        
        return None
    
    def play(self):
       
        #Evaluar si efectivamente es un solo caracter alfabético
        if  len(self.letra)>1 or len(self.letra)==0:
            print("\t\nYou entered more than one character or none.\nYou must write one character at a time. (-1 of attempt)\n")
            self.attempt=self.attempt - 1
        elif (self.letra).isalpha()==False:
            print("\t\nYou entered a character that does not belong to the alphabet. (-1 of attempt)\n")
            self.attempt=self.attempt - 1
        elif self.letra not in self.word:
            print("hat letter is not in the word. (-1 of attempt)\n")
            self.attempt=self.attempt - 1
        else:
            print("Good!") #Si acierta, imprime esto y no quita vida
            #Reemplazar los asteriscos por los caracteres ya hallados que esten en la palabra
            for index in range(len(self.word)):
                if self.letra==self.word[index]:
                    self.lista[index]=self.letra
                    
        print(''.join(self.lista)) #Imprimir el avance
        return None
    
    def win(self):
       
        if '*' not in self.lista: #Si adivina antes de gastar sus oportunidades, gana
            print("\n\nYou have won, the word is: {0}\nCongratulations!".format(self.word))
            if self.word not in self.discovered:
                (self.discovered).append(self.palabra) #Si es la primera vez que la descubre, añadirla a la lista
            return True #Si ya ganó, salir del loop
   
    def loss(self):
       
        if '*' in self.lista:
            print("\n\nyou lost. :c")
        return None
    
    def descubierta(self):
        
        if self.word in self.discovered:
               print("\n\t>>You've guessed this word before<<") #Si ya la descubrió anteriormente, darle una pista
        if len(self.discovered)>0:
                print("\nYour words discovered so far are the following:\n{0}".format(' '.join(self.descubiertas)))
        return None
    
    def goodbye():
        
        try:
            status=int(input("Play again?\t\nYES: press 1\t\nNO: press 0\n"))
            if status==1:
                return True
            elif status==0:
                print("\nSee you soon...")
                return False
            else:
                print("I didn't understand your answer, do it again:")
                return Game.goodbye()
        except:
            print("I didn't understand your answer, do it again:")
            return Game.goodbye()
        
    def status(self):
        
        self.flag= Game.goodbye()
        
        return self.flag
    
#MAIN

juego=Game()
#statuss=juego.flag

while juego.flag==True:
    
    juego.random_word()
    juego.descubierta()
    juego.init_asteriscos()
    juego.life_counter_status()
    
    while (juego.attempt) > 0:
        
        juego.letter()
        juego.play()
        juego.life_counter_status()
        
        if juego.win()==True:
            break
        
    juego.loss()
    
    juego.status()