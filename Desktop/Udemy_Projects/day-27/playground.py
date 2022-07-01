def add(*args):
    sum=0
    for n in args:
        sum+=n
    return sum


def calculate(**kwargs):
    for key,value in kwargs.items():
        print(key)



calculate(add=3,multiply=5)
