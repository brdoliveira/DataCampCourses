def foo(x):
    x[0] = 99

my_list = [1,2,3]
foo(my_list)
print(my_list)

def bar(x):
    x = x + 90

my_var = 3
bar(my_var)
print(my_var)

a = [1,2,3]
b = a
a.append(4) 
print(a)

def foo(var=[]):
    var.append(1)
    return var

foo()
print(foo())
print(foo())
print(foo())

def foo(var=None):
    if var is None:
        var = []
    var.append(1)
    return var

print(foo())
print(foo())