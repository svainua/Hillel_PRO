def deco(func: function):
    def inner():
        print("running inner() ")


    return inner


@deco
def target():
    print("running target()")


target()
