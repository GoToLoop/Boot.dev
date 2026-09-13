def args_logger(*args: object, **kwargs: object):
    print(*(f"{idx}. {arg}" for idx, arg in enumerate(args, 1)), sep='\n')
    print(*(f"* {key}: {kwargs[key]}" for key in sorted(kwargs)), sep='\n')
