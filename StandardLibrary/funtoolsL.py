import functools

"cached_property"
class cl():

    @functools.cached_property
    def fun(self):
        a1 = 1*10
        return a1

    def fun1(self,a):
        a1 = a*100
        return a1

cl1 =cl()
print(cl1.fun)
print(cl1.fun1(10))
print(cl1.fun)
print(cl1.fun1(10))