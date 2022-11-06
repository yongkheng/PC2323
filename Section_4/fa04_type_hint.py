from typing import Union

def square(x : Union[int, float]) -> Union[int, float]:
    return x*x

print(square(12345))
print(square(1.2345))
print(square('12345'))

