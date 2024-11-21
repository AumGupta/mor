# Python Anomalies and How to Handle Them

This repository explores various Python anomalies, explains why they occur, and provides ways to handle them effectively.

## 1. Floating-Point Arithmetic Errors
**Explanation:** Floating-point numbers are approximations, so calculations involving them can produce unexpected results due to limitations of the IEEE 754 standard.

**How to Handle:** Use the `decimal` module or `math.isclose()` to manage floating-point precision issues.

#### Example (Anomaly):

```python
print(0.1 + 0.2)  # Output: 0.30000000000000004
print(0.3 - 0.2 == 0.1)  # Output: False
```

#### Example (Handling):

```python
from decimal import Decimal
print(Decimal('0.1') + Decimal('0.2'))  # Output: 0.3

import math
print(math.isclose(0.3 - 0.2, 0.1))  # Output: True
```

## 2. Mutable Default Arguments
**Explanation:** Default mutable arguments retain state between function calls because they are evaluated once when the function is defined.

**How to Handle:** Use immutable defaults like `None` and initialize the mutable object inside the function.

#### Example (Anomaly):

```python
def append_to_list(value, lst=[]):
    lst.append(value)
    return lst

print(append_to_list(1))  # Output: [1]
print(append_to_list(2))  # Output: [1, 2] (same list reused!)
```

#### Example (Handling):

```python
def append_to_list(value, lst=None):
    if lst is None:
        lst = []
    lst.append(value)
    return lst

print(append_to_list(1))  # Output: [1]
print(append_to_list(2))  # Output: [2]
```

## 3. NaN is Not Equal to Itself
**Explanation:** `NaN` (Not a Number) is not equal to itself, as per the IEEE 754 standard for floating-point arithmetic.

**How to Handle:** Use `math.isnan()` or `numpy.isnan()` to explicitly check for `NaN` values.

#### Example (Anomaly):

```python
import math
print(math.nan == math.nan)  # Output: False
```

#### Example (Handling):

```python
import math
print(math.isnan(math.nan))  # Output: True
```

