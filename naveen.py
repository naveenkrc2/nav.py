clsss abc:
def sum(self,a,b):
self.a=a
self.b=b
c=a+b
print(c)
class abc1(abc):
def sub1(self,a,b):
sel.a=a
sel.b=b
c=a-b
print(c)
class abc2(abc1):
def mult1(self,a,b):
self.a=a
self.b=b
c=a*b
print(c)
obj=abc2()
obj.sum(2,3)
obj.sub1(4,2)
obj.mult1(3,5)
