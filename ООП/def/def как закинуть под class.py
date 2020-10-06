# OOП - def под class  - how to add all def под класс
class Dice: 
    
    @property # its getattr    or property(fget=def)
    def number(self):
        return choice(range(1,6+1))
    
d = Dice()
