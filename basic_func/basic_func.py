def add(a, b):
    return a+b


def sub(a, b):
    return a-b


def mul(a, b):
    return a*b


def div(a, b):
    return a/b


def power(base, pow):
    return base ** pow


def square(base):
    return base*base

def greet(이름="낯선자", 나이=20):
    인사 =""
    if 나이 > 30:
        인사 = "안녕하십니까"
    elif 나이 < 19:
        인사 = "안녕"
    else:
        인사 = "안녕하신가"
    return 인사 + " " + f"{이름}!"