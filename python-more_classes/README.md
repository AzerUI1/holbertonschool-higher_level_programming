# Python Classes, Objects, and Decorators

## Classes and Objects

### What are Classes?
Classes are blueprints for creating objects in Python. They define the structure and behavior of objects.

### Basic Class Syntax
```python
class ClassName:
    """Optional class documentation string"""
    
    def __init__(self, parameters):
        # Constructor method - initializes new objects
        self.attributes = values
    
    def method_name(self, parameters):
        # Method definition
        pass
```

### Example: Simple Class
```python
class Dog:
    """A simple Dog class"""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.tricks = []
    
    def bark(self):
        return f"{self.name} says Woof!"
    
    def add_trick(self, trick):
        self.tricks.append(trick)
    
    def get_info(self):
        return f"{self.name} is {self.age} years old and knows {len(self.tricks)} tricks"

# Creating objects (instances)
dog1 = Dog("Buddy", 3)
dog2 = Dog("Lucy", 5)

print(dog1.bark())  # Output: Buddy says Woof!
dog1.add_trick("sit")
print(dog1.get_info())  # Output: Buddy is 3 years old and knows 1 tricks
```

### Class Attributes vs Instance Attributes
```python
class Car:
    # Class attribute - shared by all instances
    wheels = 4
    
    def __init__(self, brand, model):
        # Instance attributes - unique to each instance
        self.brand = brand
        self.model = model

car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Civic")

print(car1.wheels)  # Output: 4
print(car2.wheels)  # Output: 4
print(Car.wheels)   # Output: 4
```

### Inheritance
```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        raise NotImplementedError("Subclass must implement this method")

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

class Duck(Animal):
    def speak(self):
        return f"{self.name} says Quack!"

cat = Cat("Whiskers")
duck = Duck("Donald")

print(cat.speak())  # Output: Whiskers says Meow!
print(duck.speak()) # Output: Donald says Quack!
```

### Special Methods (Magic/Dunder Methods)
```python
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        return f"'{self.title}' by {self.author}"
    
    def __len__(self):
        return self.pages
    
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

book1 = Book("Python Basics", "John Doe", 300)
book2 = Book("Python Basics", "John Doe", 300)

print(str(book1))    # Output: 'Python Basics' by John Doe
print(len(book1))    # Output: 300
print(book1 == book2) # Output: True
```

## Decorators

### What are Decorators?
Decorators are functions that modify the behavior of other functions or methods without permanently modifying them.

### Function Decorators
```python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Something is happening before the function is called.
# Hello!
# Something is happening after the function is called.
```

### Decorators with Arguments
```python
def repeat(num_times):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(num_times=3)
def greet(name):
    print(f"Hello {name}")

greet("Alice")
# Output:
# Hello Alice
# Hello Alice
# Hello Alice
```

### Class Decorators
```python
def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class Database:
    def __init__(self):
        print("Database created")

db1 = Database()
db2 = Database()
print(db1 is db2)  # Output: True
```

### Built-in Decorators

#### @property
```python
class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value
    
    @property
    def area(self):
        return 3.14159 * self._radius ** 2

circle = Circle(5)
print(circle.area)    # Output: 78.53975
circle.radius = 10
print(circle.area)    # Output: 314.159
```

#### @classmethod and @staticmethod
```python
class Calculator:
    calculation_type = "Basic Arithmetic"
    
    def __init__(self, value=0):
        self.value = value
    
    @classmethod
    def get_calculation_type(cls):
        return cls.calculation_type
    
    @staticmethod
    def add_numbers(a, b):
        return a + b
    
    def instance_method(self):
        return f"Current value: {self.value}"

print(Calculator.get_calculation_type())  # Output: Basic Arithmetic
print(Calculator.add_numbers(5, 3))       # Output: 8

calc = Calculator(10)
print(calc.instance_method())             # Output: Current value: 10
```

### Practical Example: Timing Decorator
```python
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds to execute")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(2)
    return "Done!"

result = slow_function()
# Output: slow_function took 2.0001 seconds to execute
```

### Decorator with Preserved Metadata
```python
from functools import wraps

def debug(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper

@debug
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Alice"))
# Output:
# Calling greet with args: ('Alice',), kwargs: {}
# greet returned: Hello, Alice!
# Hello, Alice!
```

## Key Concepts Summary

### Classes & Objects:
- **Classes**: Blueprints for creating objects
- **Objects**: Instances of classes with their own state
- **Inheritance**: Creating new classes from existing ones
- **Polymorphism**: Same interface, different implementations
- **Encapsulation**: Bundling data and methods together

### Decorators:
- **Function Decorators**: Modify function behavior
- **Class Decorators**: Modify class behavior
- **Built-in Decorators**: @property, @classmethod, @staticmethod
- **Chaining**: Multiple decorators can be applied
- **Metadata**: Use @wraps to preserve function metadata

This combination of classes, objects, and decorators provides a powerful foundation for object-oriented programming and metaprogramming in Python.
