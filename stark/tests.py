from django.test import TestCase

# Create your tests here.
class Singleton:
    def __init__(self,name):
        self.name=name

    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls)
        return cls._instance

one = Singleton('aa')
two = Singleton('bb')
print(one.name)
print(one.name)



two.a = 3
print(one.a)
# one和two完全相同,可以用id(), ==, is检测
print(id(one))
print(id(two))
print(one == two)
print(one is two)