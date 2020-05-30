class PartyAnimal:
    x = 0
    
    def party(self):
        self.x = self.x + 1
        print('So Far', self.x)

an = PartyAnimal()

print(type(an))
print(dir(an))

an.party()
an.party()
an.party()