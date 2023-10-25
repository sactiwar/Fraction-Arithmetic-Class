
class Fraction:

    def __init__(self,x,y):
        self.numerator = x
        self.denominator = y

    def __str__(self):
        return "{}/{}".format(self.numerator,self.denominator)

    def __add__(self, other):
        new_nu = self.numerator*other.denominator + self.denominator * other.numerator
        new_de = self.denominator * other.denominator
        return '{} + {} = {}/{}'.format(self,other,new_nu,new_de)


    def __sub__(self, other):
        new_nu = self.numerator * other.denominator - self.denominator * other.numerator
        new_de = self.denominator * other.denominator
        return '{} - {} = {}/{}'.format(self,other,new_nu, new_de)

    def __mul__(self, other):
        new_nu = self.numerator * other.numerator
        new_de = self.denominator * other.denominator
        return '{} X {} = {}/{}'.format(self,other,new_nu, new_de)

    def __truediv__(self, other):
        new_nu = self.numerator * other.denominator
        new_de = self.denominator * other.numerator
        return '{} / {} = {}/{}'.format(self,other,new_nu, new_de)
