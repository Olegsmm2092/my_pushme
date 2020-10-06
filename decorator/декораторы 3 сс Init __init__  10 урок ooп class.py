#@def - конвертер - class to obj
# name = 'unit1'
#инструмент - def with @def  -конвертер - how to cc fe any init it __init__() \n

class Person:
    name = 'Oleg'
    
    @classmethod # will be конвертер class to obj
    def change_name(cls, name):
            cls.name = name
            
p = Person()
print(p.__dict__)
p.change_name('unit3')

print('instance dict:', p.__dict__)

print('person name:', Person.name)
