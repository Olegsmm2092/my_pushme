'''
Basic - class - @def - 

св - how to add 1 more fe surname

'''


class Person:
    def __init__(self, name):
        self._name = name
#         self._surname = surname
        
#     def at_obj(self, obj) #ВНИМАТЕЛЬНЕЕ ошибка cls
#     @classmethod # конвертер at class to obj
#     def at_obj(cls, obj):
#         #check
#         if hasattr(obj, name, surname):
#             name = getattr(obj, name, surname)
#             return cls(name=name, surname=surname)
#         return cls

    @classmethod # конвертер at class to obj
    def at_obj(cls, obj):
        print('classmethod at_obj()')
        #check
        if hasattr(obj, 'name'):
            name = getattr(obj, 'name')
#             surname = getattr(obj, 'surname)
            return cls(name=name)
        return cls
        
    def getter(self):
        print('property getter()')
#         return self._name = name  #ВНИМАТЕЛЬНЕЕ ошибка its just getter print it not show look up whats to do
        return self._name
                                    #back cuz its def  same print
    
    def setter(self, value):
        print('property name.setter()')
        self._name = value
#         self._surname = value1
    
    name = property()
#     name = getter(getter) #ВНИМАТЕЛЬНЕЕ ошибка init.word(def)
    name = name.getter(getter)
    name = name.setter(setter)
    
class Config:
    name = 'unit1'
    surname = 'sur_unit1'
#     surname = 'sur_unit1'
    
p = Person('Oleg') #fixme - get it file class  path, obj


p.__dict__
p = Person.def(class)
p.__dict__
    
