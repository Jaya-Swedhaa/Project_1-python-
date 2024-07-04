# simple generator

def gen():
    yield "a"
    yield "b"
    yield "c"
    yield 2
    yield 4

x= gen()
print(next(x))

for i in x:
    print(i)

# generator with example

gen1 = (i*2 for i in range(10) if i>=5)
for x in gen1:
    print(x)