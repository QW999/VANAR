
def f(a, b, c=0):
    return a, b, c
print(f(1, 2, 3))



def wrapp(content, prefix, suffix):
    return prefix + content + suffix
print(wrapp("Hello", "[", "]"))
print(wrapp(prefix="[", content="Hello",  suffix="]"))


def wrapp(content, prefix="", suffix=""):
    return prefix + content + suffix
print(wrapp("Hello"))