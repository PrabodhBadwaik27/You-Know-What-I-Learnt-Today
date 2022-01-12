def Capital(function):
    def wrapper():
        fun = function()
        out = fun.upper()
        return out
    return wrapper


@Capital
def Plain():
    inp = input('Type something: ')
    return inp


print(Plain())
