def log(filename=None):
    def my_decorator(func):
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
def my_function_yes_file(x, y):
    return x + y


@log()
def my_function_no_file(x, y):
    return x + y


# my_function(6, 2)
# my_function(2,0)
