'''
要求：
写一个装饰器 log_call，在函数调用前后打印日志：
调用前打印："开始调用 {函数名}"
调用后打印："结束调用 {函数名}"
返回原函数的结果

用这个装饰器装饰两个函数：
@log_call
def greet(name: str) -> str:
    return f"你好，{name}"

@log_call
def add(a: int, b: int) -> int:
    return a + b

测试：
print(greet("mengjie"))
print(add(1, 2))

预期输出：
开始调用 greet
结束调用 greet
你好，mengjie
开始调用 add
结束调用 add
3

提示：
装饰器结构：def log_call(func): def wrapper(*args, **kwargs): ... return wrapper
func.__name__ 获取函数名
别忘了 return func(*args, **kwargs)
'''

def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"开始调用 {func.__name__}")
        result = func(*args, **kwargs)
        print(f"结束调用 {func.__name__}")
        return result
    return wrapper

@log_call
def greet(name: str) -> str:
    return f"你好，{name}"

@log_call
def add(a: int, b: int) -> int:
    return a + b

print(greet("mengjie"))
print(add(1, 2))