

from home_4 import klass_1, klass_2, klass_3, klass_4

class klass_5(klass_1, klass_2, klass_3, klass_4):
    
    
    def __init__(self,age):
        self._age = age

    @property
    def age(self):
        return  self._age

    atribut_klass_1 = klass_1('Kasymbek')
    print(atribut_klass_1)


    atribut_klass_2 = klass_2('16')
    print(atribut_klass_2)

    met_1 = klass_3()
    met_1.method_1()

    met_2 = klass_4()
    met_2.method_2()

