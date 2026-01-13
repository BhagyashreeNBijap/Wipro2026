add=lambda a,b: a+b
print(add(8,4))

multi=lambda c,d: c*d
print(multi(8,4))

multi=lambda c,d: c*d
print(multi(100,20))

maxnum=lambda x,y: x if x>y else y
print(maxnum(10,40))

#map(function,iterable)
numbers=[1,2,3,4,5]
result=map(lambda x:x*2,numbers)
print(list(result))

nos=[5,6,4,8]
result=map(lambda x:x*5,nos)
print(list(result))
