import inspect
from pprint import pprint

def introspection_info(obj):
    result = {}
    result['type'] = type(obj).__name__
    result['attributes'] = [name for name, value in inspect.getmembers(obj) if not callable(value)]
    result['methods'] = [name for name, value in inspect.getmembers(obj) if callable(value)]
    result['module'] = inspect.getmodule(introspection_info).__name__
    return result

number_info = introspection_info(42)
print(number_info)
