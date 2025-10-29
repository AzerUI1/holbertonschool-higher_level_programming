🧪 Test-Driven Development (TDD) in Python
<p align="center"> <img src="https://miro.medium.com/v2/resize:fit:800/format:webp/1*0g0RkEjlD6FzFh42Q87czQ.png" width="300"> </p>

Test-Driven Development (TDD) is a software development approach where you write tests before writing the actual code.
It helps developers produce cleaner, bug-free, and maintainable code ✅

🔹 Why TDD?
Benefit	Description
✅ Better code quality	Catch bugs early
✅ Maintainable	Easier to refactor
✅ Documentation	Tests explain how code works
✅ Confidence	Ensures code works as intended
🔹 TDD Workflow

Write a Test → Describe the functionality you want

Run the Test → It should fail initially

Write Code → Implement minimal code to pass the test

Run the Test Again → Ensure it passes

Refactor → Clean up the code without breaking the test

Repeat → For every new feature

<p align="center"> <img src="https://miro.medium.com/v2/resize:fit:720/format:webp/1*dNc7EtGnq9c9Q0rZ-UGgQg.png" width="500"> </p>
🔹 Example in Python using unittest
# test_math.py
import unittest
from math_ops import add  # math_ops.py will contain the function

class TestMathOps(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

if __name__ == "__main__":
    unittest.main()

# math_ops.py
def add(a, b):
    return a + b


Workflow:

Write test_add → initially fails (if add doesn’t exist)

Implement add → test passes ✅

Refactor if necessary → test ensures correctness

🔹 Writing More Tests
def subtract(a, b):
    return a - b

# test
self.assertEqual(subtract(5, 3), 2)
self.assertEqual(subtract(0, 10), -10)


✅ Each function gets a corresponding test
✅ Ensures edge cases are handled

🔹 Popular Python Testing Frameworks
Framework	Purpose
unittest	Built-in, simple tests
pytest	Powerful, easy to use
nose2	Extends unittest
doctest	Test examples in docstrings

Example with pytest:

# test_math_pytest.py
from math_ops import add

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


Run:

pytest

🔹 Best Practices

✅ Write small, focused tests
✅ Keep tests independent
✅ Cover edge cases
✅ Refactor code after passing tests
✅ Use descriptive test names

📚 Learn More — Buttons
<p align="center"> <a href="https://docs.python.org/3/library/unittest.html"> <img src="https://img.shields.io/badge/Python-unittest-blue?style=for-the-badge&logo=python"> </a> <a href="https://docs.pytest.org/en/stable/"> <img src="https://img.shields.io/badge/PyTest-Docs-green?style=for-the-badge"> </a> <a href="https://martinfowler.com/bliki/TestDrivenDevelopment.html"> <img src="https://img.shields.io/badge/MartinFowler-TDD-red?style=for-the-badge"> </a> </p>
✅ Summary Table
Step	Description
Write Test	Define what code should do
Run Test	Ensure it fails first
Implement Code	Make test pass
Run Test	Confirm success
Refactor	Improve code without breaking test
🎯 Conclusion

TDD ensures robust, reliable, and clean code.
Start with tests → code with confidence → refactor safely ✅
