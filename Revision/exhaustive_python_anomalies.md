# Python Anomalies and Behaviors

## 1. Floating-Point Arithmetic Errors
Floating-point numbers are approximations, so calculations involving them can produce unexpected results.
#### Example:

```python
print(0.1 + 0.2)  # Output: 0.30000000000000004
print(0.3 - 0.2 == 0.1)  # Output: False
```

## 2. Mutable Default Arguments
Using mutable objects (like lists or dictionaries) as default arguments in functions can lead to surprising behavior.
#### Example:

```python
def append_to_list(value, lst=[]):
    lst.append(value)
    return lst

print(append_to_list(1))  # Output: [1]
print(append_to_list(2))  # Output: [1, 2] (same list is reused!)
```

## 3. NaN is Not Equal to Itself
`NaN` (Not a Number) is not equal to itself, as per IEEE 754 floating-point standard.
#### Example:

```python
import math
print(math.nan == math.nan)  # Output: False
```

## 4. Integer Overflow Doesn't Exist
Python integers have arbitrary precision, unlike many other languages where integers have fixed sizes.
#### Example:

```python
x = 2 ** 1000
print(x)  # Huge number without overflow
```

## 5. Chained Comparisons
Python allows chaining comparisons for readability, but it can sometimes be confusing.
#### Example:

```python
print(1 < 2 < 3)  # Output: True
print(1 < 3 > 2)  # Output: True
```

## 6. Unexpected Boolean Conversion
In Python, non-zero numbers and non-empty collections are `True`, while `0`, `None`, and empty collections are `False`.
#### Example:

```python
print(bool([]))  # Output: False
print(bool([0]))  # Output: True (list is non-empty!)
```

## 7. String Immutability
Strings in Python are immutable, so operations that modify them create new objects instead.
#### Example:

```python
s = 'hello'
s += ' world'
print(s)  # Output: 'hello world' (creates a new string)
```

## 8. Variable Name Shadowing
Loop variables can 'leak' outside the loop scope, leading to unintended behavior.
#### Example:

```python
for i in range(5):
    pass

print(i)  # Output: 4 (loop variable is accessible)
```

## 9. Implicit Type Conversion
Python allows implicit type conversion, which can lead to unexpected results.
#### Example:

```python
print(0.1 + 1)  # Output: 1.1
print('10' * 2)  # Output: '1010' (not 20)
```

## 10. Hash Collisions in Dictionaries
Objects with the same hash value may overwrite each other when used as dictionary keys.
#### Example:

```python
class AlwaysEqual:
    def __eq__(self, other):
        return True
    def __hash__(self):
        return 42

a = AlwaysEqual()
b = AlwaysEqual()
d = {a: 'first', b: 'second'}
print(d)  # Output: {<AlwaysEqual object>: 'second'}
```

