def my_function():
    return 42

x = my_function

my_function()
x()

def foo():
    x = [3,6,9]

    def bar(y):
        print(y)

    for value in x:
        bar(x)


def ifs(x,y):
    if x > 4 and x < 10 and y > 4 and y < 10:
        print(x * y)

def ranges(x,y):
    def in_range(v):
        return v > 4 and v < 10

    if in_range(x) and in_range(y):
        print(x * y)

def new_function():
    def print_me(s):
        print(s)

    return print_me

new_func = new_function()
new_func('This is a sentence.')