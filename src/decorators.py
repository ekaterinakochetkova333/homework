def log(filename=None):
    def my_decorator(func):     #my_function
        def wrapper(*args, **kwargs):
            result = None
            file = None
            text = ""
            if filename is not None:
                file = open(filename, "w+")
            try:
                result = func(*args, **kwargs)
                text = f'{func.__name__} ok'
            except Exception as e:
                text = f'{func.__name__} error: {type(e).__name__} Inputs: {args} {kwargs}'
            finally:
                if file is not None:
                    file.write(text)
                    file.close()
                else:
                    print(text)
            return result
        return wrapper
    return my_decorator


@log(filename="mylog.txt")
def my_function(x, y):
    return x + y

my_function(1, 2)
