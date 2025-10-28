# 🐍 Python Data Structures: A Wonder-Filled Guide 🌟

Welcome to the magical world of Python data structures! This guide will take you on an enchanting journey through the fundamental building blocks that make Python such a powerful and elegant programming language.

## 📚 Table of Contents
- [Basic Data Structures](#basic-data-structures)
- [Advanced Data Structures](#advanced-data-structures)
- [Performance Characteristics](#performance-characteristics)
- [Practical Examples](#practical-examples)
- [Best Practices](#best-practices)

---

## 🎯 Basic Data Structures

### 1. Lists 📋 - The Versatile Workhorses

```python
# ✨ Creating lists
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]

# 🎩 List magic operations
fruits.append("orange")          # Add to end
fruits.insert(1, "blueberry")    # Insert at position
fruits.remove("banana")          # Remove element
popped = fruits.pop()            # Remove and return last element

# 🔥 List comprehensions (Pure Python magic!)
squares = [x**2 for x in range(10)]
even_squares = [x**2 for x in range(10) if x % 2 == 0]
```

### 2. Tuples 🎭 - The Immutable Guardians

```python
# 🛡️ Creating tuples (they're immutable!)
coordinates = (4, 5)
person = ("Alice", 30, "Engineer")
single_element = (42,)  # Don't forget the comma!

# 🎯 When to use tuples?
# - When you need data integrity
# - As dictionary keys (unlike lists!)
# - Function return multiple values
def get_stats(numbers):
    return min(numbers), max(numbers), sum(numbers)/len(numbers)
```

### 3. Dictionaries 🗝️ - The Key-Value Magicians

```python
# 🔑 Creating dictionaries
student = {
    "name": "John Doe",
    "age": 21,
    "grades": [85, 92, 78]
}

# 🎩 Dictionary wizardry
student["email"] = "john@email.com"      # Add new key
age = student.get("age", "N/A")          # Safe access
keys = student.keys()                    # View of keys
values = student.values()                # View of values

# ✨ Dictionary comprehensions
square_dict = {x: x**2 for x in range(5)}
```

### 4. Sets 🎪 - The Unique Collectors

```python
# 🌟 Creating sets
unique_numbers = {1, 2, 3, 4, 5}
colors = set(["red", "blue", "green"])

# 🎭 Set operations (mathematical magic!)
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

union = A | B           # {1, 2, 3, 4, 5, 6}
intersection = A & B     # {3, 4}
difference = A - B       # {1, 2}
```

---

## 🚀 Advanced Data Structures

### 5. Collections Module 🎁 - The Specialized Toolkit

```python
from collections import deque, Counter, defaultdict, namedtuple

# 🎯 Deque - Fast appends and pops from both ends
queue = deque(["Alice", "Bob", "Charlie"])
queue.append("David")    # Add to right
queue.popleft()          # Remove from left

# 🔢 Counter - Count hashable objects
word_count = Counter("abracadabra")
# Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})

# 🏠 Defaultdict - Dictionaries with default values
fruit_basket = defaultdict(list)
fruit_basket['tropical'].append('mango')

# 🏷️ Namedtuple - Self-documenting tuples
Point = namedtuple('Point', ['x', 'y'])
p = Point(11, y=22)
print(p.x, p.y)  # 11 22
```

### 6. Heapq 📚 - The Priority Queue

```python
import heapq

# 📊 Min-heap implementation
numbers = [5, 7, 9, 1, 3]
heapq.heapify(numbers)           # Transform list into heap
heapq.heappush(numbers, 4)       # Push element
smallest = heapq.heappop(numbers) # Pop smallest element

# 🎯 Practical example - Priority scheduling
tasks = []
heapq.heappush(tasks, (2, "Medium priority task"))
heapq.heappush(tasks, (1, "High priority task"))
heapq.heappush(tasks, (3, "Low priority task"))

next_task = heapq.heappop(tasks)  # Gets high priority task first
```

### 7. Arrays 💾 - Memory-Efficient Numeric Storage

```python
import array

# 💰 More memory efficient than lists for numeric data
int_array = array.array('i', [1, 2, 3, 4, 5])
float_array = array.array('f', [1.0, 2.5, 3.7])

# Type codes: 'i' for int, 'f' for float, 'd' for double
```

---

## ⚡ Performance Characteristics

| Operation | List | Dict | Set | Deque |
|-----------|------|------|-----|-------|
| Append | O(1) | - | - | O(1) |
| Prepend | O(n) | - | - | O(1) |
| Insert | O(n) | - | - | O(n) |
| Delete | O(n) | O(1) | O(1) | O(n) |
| Search | O(n) | O(1) | O(1) | O(n) |
| Access | O(1) | O(1) | - | O(n) |

---

## 🎨 Practical Examples

### 🎯 Real-World Use Cases

```python
# 🛒 E-commerce shopping cart
class ShoppingCart:
    def __init__(self):
        self.items = {}  # product_id: quantity
    
    def add_item(self, product_id, quantity=1):
        self.items[product_id] = self.items.get(product_id, 0) + quantity
    
    def get_total_items(self):
        return sum(self.items.values())

# 📊 Data analysis with Counter
def analyze_text(text):
    words = text.lower().split()
    word_freq = Counter(words)
    return word_freq.most_common(5)

# 🎮 Game leaderboard with heapq
class Leaderboard:
    def __init__(self):
        self.scores = []
    
    def add_score(self, player, score):
        heapq.heappush(self.scores, (-score, player))  # Negative for max-heap
    
    def get_top_players(self, n=3):
        return [heapq.heappop(self.scores) for _ in range(min(n, len(self.scores)))]
```

### 🔮 Advanced Patterns

```python
# 🌈 Dictionary with default factories
from collections import defaultdict

def nested_dict():
    return defaultdict(nested_dict)

config = nested_dict()
config['database']['host'] = 'localhost'
config['database']['port'] = 5432

# 🎭 Multiple return values with namedtuple
from typing import NamedTuple

class AnalysisResult(NamedTuple):
    mean: float
    median: float
    mode: float
    successful: bool

def analyze_data(data):
    # ... calculations ...
    return AnalysisResult(mean=5.5, median=6.0, mode=7.0, successful=True)
```

---

## 💫 Best Practices

### 🎯 Choosing the Right Data Structure

```python
# ✅ Use lists when:
# - You need ordered collection
# - You need to modify the collection
# - You need indexing

# ✅ Use tuples when:
# - Data shouldn't change
# - Using as dictionary keys
# - Multiple return values

# ✅ Use dictionaries when:
# - You need key-value pairs
# - Fast lookups by key
# - Mapping relationships

# ✅ Use sets when:
# - You need uniqueness
# - Mathematical set operations
# - Fast membership testing
```

### 🚀 Performance Tips

```python
# 🐇 Use list comprehensions
# Slow 🐢
result = []
for x in range(1000):
    if x % 2 == 0:
        result.append(x**2)

# Fast 🐇
result = [x**2 for x in range(1000) if x % 2 == 0]

# 🎯 Use sets for membership testing
# Slow 🐢
if item in list_of_thousands:

# Fast 🐇
if item in set_of_thousands:

# 🔧 Use the right tool for the job
from collections import deque

# For queues (FIFO)
queue = deque()
queue.append('task1')
queue.popleft()

# For stacks (LIFO)
stack = deque()
stack.append('task1')
stack.pop()
```

---

## 🌟 Conclusion

Python's data structures are like a wizard's toolkit - each has its own special magic! Mastering them will make you a more effective Python programmer and open up new possibilities for solving problems elegantly and efficiently.

Remember: **"Choose the right tool for the job!"** 🛠️

Happy coding! 🎉🐍

---

*"Data structures are the building blocks of elegant solutions."* ✨

