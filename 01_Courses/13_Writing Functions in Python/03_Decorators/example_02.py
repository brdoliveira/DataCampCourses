x = 7
y = 200

print(x)

def foo():
    x = 42
    print(x)
    print(y)

foo()

print(x)

# ---------------------------

x = 30
y = 300

print(x)

def foo():
    global x
    x = 60
    print(x)
    print(y)

foo()

print(x)

# ------------------------------
def foo():
    x = 10

    def bar():
        nonlocal x
        x = 200

    print(x)

    bar()
    print(x)

foo()