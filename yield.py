# yield--- yield is like a return , but instead of returning once , it returns a sequence of values one by one 
def simple_generator():
    yield 1
    yield 2 
    yield 3 

for value in simple_generator():
    print(value)