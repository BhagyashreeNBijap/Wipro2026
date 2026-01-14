def numbers():
    yield 1
    yield 2
    yield 3

gen=numbers()
print(next(gen))
print(next(gen))
print(next(gen))

def count_up(n):
    for i in range(1,n+1):
        yield i

for val in count_up(4):
        print(val)
