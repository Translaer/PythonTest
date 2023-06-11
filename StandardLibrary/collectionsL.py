"""
容器类模块
"""

import collections

"Counter"
"重复计数"
# a = "hello world! hello world! hello world!"
# b = "hello world! hello world!"
# d0 = {"a":1,"b":2}
# d1 = (1,2,3,34,5,8,5 )
# d2 = [1,2,3,54,"z","aza"]
# d3 = {"a":"sss","b":"ssss"}
# a = [0,1,2,3,0,1,5,"a"]
# c1 = collections.Counter()
# c2 = collections.Counter()
# c1.update(a)
# c1.update(d0)
# c1.update(d1)
# c1.update(d2)
# c1.update(d3)
# c2.update(b)
# print(c1)
# print(c1["hello"])
# c1.update(b.split())
# print(c1)
# for i in c1.elements():
#     print(i)
# for i in c1.most_common(3):
#     print(i)
# print(c1)
# print(c2)
# print(c1+c2)

"defaultdict"
"具备初始值的字典"
# def fun():
#     return "de va"
# d = collections.defaultdict(fun,foo= "bar")
# a = {"a0":1,"a2":2}
# b = {"b0":1,"b2":2}
# d0 = collections.defaultdict(int,**a)
# print(d)
# print(d["foo"])
# print(d["foo1"])
# print(d0)
# print(d0["foo"]
# print(d0["foo1"])
# for i in d0.items():
#     print(i)
# d0.update(b)
# for i in d0.items():
#     print(i)

"deque"
"队列，可旋转，类似于拨码电话转盘"
# d = collections.deque(range(10))
# print(d)
# print(d.__len__())
# print(d[0])
# print(d[-1])
# d = collections.deque()
# d.extend(range(10,15))
# print(d)
# d.append(16)
# print(d)
# d.extend(range(17,20))
# print(d)
# d.appendleft(9)
# print(d)
# d.extendleft(range(5,8))
# print(d)
# print(d[0])
# print(d[-1])
# d.rotate(2)
# print(d)
# d.rotate(-2)
# print(d)

"nametuple"
"命名元组，元组的基础上具备了键"
# Person = collections.namedtuple("person", ("age", "wight", "male","famimly"))
# p1 = Person(18,20,30,("father","mother"))
# print(p1._fields)
# print(p1._asdict())
# print(p1)
# print(p1[0])
# print(p1[0].imag)
# print(p1[1:3])
# for i in p1:
#     print(i)

"chainMap"
"合并多个映射，仅仅保存多映射的引用，省内存"
# a = {"a0":1,"a1":2}
# a1 = {"a0":1.1,"a1":2.2}
# b = {"b0":10,"b1":20}
# c = {"c0":100,"c1":200}
# m = collections.ChainMap(a,b,c,a1)
# print(m["a0"])
# m['a0'] = 1.2
# print(a1['a0'])
# for i in m:
#     print(i)
