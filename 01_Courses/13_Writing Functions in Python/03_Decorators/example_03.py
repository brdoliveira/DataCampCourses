def foo():
    a = 5
    def bar():
        print(a)
    return bar

func = foo()

func() # 5

"""
print(type(func.__closure__))
print(len(func.__closure__))
print(func.__closure__[0].cell_contents)

# outer function
def parent():
    # nested function
    def child():
        pass
    return child
"""

def parent(arg_1,arg_2):
    # From child()'s point of view,
    # `value` and `my_dict` are nonlocal variables,
    # as are `arg_1` and `arg_2`
    value = 22
    my_dict = {'chocolate':'yummy'} 

    def child():
        print(2 * value)
        print(my_dict['chocolate'])
        print(arg_1 + arg_2)

    return child

new_func = parent(3,2)
print([cell.cell_contents for cell in new_func.__closure__])