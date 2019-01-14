def add(a, b):
    return a+b


# 函数即对象
add2 = add


def add_wrapper():
    return add


# print(add_wrapper()(10, 19))

def cal(func, a, b):
    return func(a, b)


# print(cal(add2, 5, 6))

from time import time


def timeit(func, *args, **kwargs):  # * 表示接收的参数作为元组来处理    ** 表示接收的参数作为字典来处理
    start = time()
    func(*args, **kwargs)
    end = time()
    print(end - start)


def test1(n):
    s = 0
    for i in range(n):
        s += i*i
    return s


# timeit(test_one, 10000)

def timeit2(func):    # 闭包
    def wrapper(*args, **kwargs):
        start = time()
        func(*args, **kwargs)
        end = time()
        print(end - start)

    return wrapper


test1 = timeit2(test1)

# test1(19999999)


@timeit2
def test2(n):
    s = 0
    for i in range(n):
        s += i*i
    return s


# test2(1000000)

handlers = set()


def on_message(func):
    handlers.add(func)
    return func


@on_message
def handler(ctx):
    pass
# handler=on_message(handler)


@on_message
def handler2(ctx):
    pass


print(handlers)