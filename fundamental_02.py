

"""
1. encapsulation
2. iheritance
3. polymorphism
"""

class Segitiga:
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi

    def luas_segitiga(self):
        return self.alas * self.tinggi/2


segitiga1 = Segitiga(10,4)
print (segitiga1.luas_segitiga())
