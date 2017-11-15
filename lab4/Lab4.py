
class Animal(object):
    def __init__(self,sound,name,age,favorite_beast,make_some_nois):
        self.sound = sound
        self.name = name
        self.age = age
        self.favorite_beast = favorite_beast
        self.make_some_nois= make_some_nois
        
    def talk(self):
        print(self.sound)

    def eat(self):
        print(" "+self.favorite_beast+" "+"is cool")

    def nois(self):
        x= input("enter a number")
        print((self.make_some_nois+"                  ")*int(x))

    def description(self):
        print(self.name + "is" +self.age +"year old and loves clones "+self.favorite_color)
naruto=Animal("i am going to be the next hokage"+" "+"kazebonshin nu gotso","uzomaki_naruto",17,"kubi","y1 is the best we are better then the rest how how how how how")
naruto.talk()
naruto.eat()
naruto.nois()

class song(object):
    def __init__(self,lyrics):
        self.lyrics= lyrics

    def sing_me_a_song():
        for n in self.lyrics:
            if n==",":
                print(/n)






























        
