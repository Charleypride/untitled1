class Person():
    def fget(self):
        pass
    def fset(self,age):
        self._age = int()
    def fdel(self):
        pass
    age = property(fget,fset,fdel,"对age操作了")
p2 = Person()
p2.age = 18.95
print(p2.age)