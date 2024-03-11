import random

class weapon:
    def __init__(self, name, magazineSize):
        self.name = name
        self.magazineSize = magazineSize
        self.magazine = []
        self.set_magazine()

    def get_name(self):
        return self.name

    def set_name(self, value):
        self.name = value

    def get_magazineSize(self):
        return self.magazineSize

    def set_magazineSize(self, value):
        self.magazineSize = value

    def get_magazine(self):
        return self.magazine

    def set_magazine(self):
        self.magazine = []
        self._loadMagazine()
        
    def _loadMagazine(self):
        for i in range(int((self.magazineSize))):
            self.magazine.append(random.choice([True, False]))
        random.shuffle(self.magazine)
        
    def shoot(self, person):
        if not self.magazine:
            return
        if self.magazine[0]:
            print(f"BANG! {person.get_name()} tomou um tiro.")
            print("=============================")
            person.set_life(person.get_life() - 1)
            return self.magazine.pop(0)
        print("CLICK! A arma não disparou.")
        print("=============================")
        return self.magazine.pop(0)