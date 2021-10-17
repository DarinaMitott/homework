"""
1. Напишите параметрический декоратор, который вызывает оборачиваемую функцию
несколько раз (по умолчанию - 2).

Предусмотрите возможность продолжать повторные вызовы декорируемой функции
при возникновении в ней исключения, в таких случаях выводите сообщения об
ошибке для каждого вызова. Используйте для этого именованный аргумент
continue_on_errors со значением по умолчанию False.


2. Напишите параметрический декоратор, который проверяет количество и типы
позиционных аргументов оборачиваемой функции.

В случае любого несоответствия необходимо сгенерировать исключение TypeError.
"""
from functools import wraps


def type_check(*types):
    def _type_check(f):
        @wraps(f)
        def inner(*args, **kwargs):
            if len(types) != len(args):
                raise TypeError('invalid number of arguments')
            for i in range(len(args)):
                if not isinstance(args[i], types[i]):
                    raise TypeError(f'Positional arg #{i} has type "{type(args[i]).__name__}" but must be {types[i].__name__}')
            return f(*args, **kwargs)
        return inner
    return _type_check


def repeat(n=2, continue_on_errors=False):
    def _repeat(f):
        @wraps(f)
        def inner(*args, **kwargs):
            for _ in range(n):
                try:
                    f(*args, **kwargs)
                except Exception as error:
                    print(f'error: {repr(error)}')
                    if not continue_on_errors:
                        break
        return inner
    return _repeat
