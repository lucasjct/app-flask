class Animal: # classe principal
    #atribtos de classe
    planeta = "Terra"
    _animal_nasceu = False

    @property
    def nasceu(self):
        return self._animal_nasceu #variavel privada

    #método = função criada dentro da classe
    def nascer(self):
        self._animal_nasceu = True
        print('0i eu nasci no planeta', self.planeta)

    def comer(self):
        print('Estou comendo..crunch crunch')
#Herança
class Mamifero(Animal):
    def comer(self):
        print("Estou tomado leite")

class Oviparos(Animal):
    def nascer(self):
        print('Acabei de quebrar o ovo no', self.planeta)

#Herança multipla
class Especial(Mamifero, Oviparos):
    def nadar(self):
        print('Tchibummm')