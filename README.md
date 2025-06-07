# 🐍 Python Reviewer

Hi and welcome to my personal **Python Reviewer**! This guide is designed to be a quick reference for key Python concepts, making it easy to refresh your memory whenever you visit this repository on GitHub.

---

## 📖 Chapter 1: Mastering Lists

Lists are one of the most versatile and fundamental data structures in Python. They are **ordered**, **mutable** (changeable), and can contain **elements of different data types**.

### ✨ 1.1 Creating Lists

You can create a list by placing comma-separated elements within square brackets `[]`.

```python
# An empty list
empty_list = []

# A list of integers
numbers = [1, 2, 3, 4, 5]

# A list with mixed data types
mixed_list = [1, "hello", 3.14, True]

# You can also use the list() constructor
from_tuple = list((1, 2, 3))
```

> **💡 Pro-Tip:** The `list()` constructor is especially useful for converting other iterables (like tuples or sets) into lists.

### ⛓️ 1.2 Indexing and Slicing

Access elements by their index (starting from 0) or create sub-lists using slicing.

| Syntax | Description | Example (`numbers = [0, 1, 2, 3, 4]`) | Result |
| --- | --- | --- | --- |
| `list[i]` | Access the element at index `i` | `numbers[2]` | `2` |
| `list[-i]` | Access from the end, `-1` is the last element | `numbers[-1]` | `4` |
| `list[i:j]` | Slice from index `i` to `j-1` | `numbers[1:4]` | `[1, 2, 3]` |
| `list[:j]` | Slice from the beginning to `j-1` | `numbers[:3]` | `[0, 1, 2]` |
| `list[i:]` | Slice from index `i` to the end | `numbers[2:]` | `[2, 3, 4]` |
| `list[i:j:k]` | Slice with a step `k` | `numbers[::2]` | `[0, 2, 4]` |
| `list[::-1]` | Reverse the list | `numbers[::-1]` | `[4, 3, 2, 1, 0]` |

### 🛠️ 1.3 Modifying Lists

Since lists are mutable, you can change, add, and remove elements.

#### Adding Elements

- `append()`: Adds an element to the end of the list.
- `insert()`: Inserts an element at a specified position.
- `extend()`: Adds all elements of an iterable to the end of the list.

```python
fruits = ["apple", "banana"]
fruits.append("cherry")
# fruits is now ['apple', 'banana', 'cherry']

fruits.insert(1, "orange")
# fruits is now ['apple', 'orange', 'banana', 'cherry']

more_fruits = ["strawberry", "blueberry"]
fruits.extend(more_fruits)
# fruits is now ['apple', 'orange', 'banana', 'cherry', 'strawberry', 'blueberry']
```

#### Removing Elements

- `remove()`: Removes the first occurrence of a specified value.
- `pop()`: Removes and returns the element at a specified index (or the last item if not specified).
- `clear()`: Removes all elements from the list.
- `del`: A keyword to remove an item or a slice.

```python
fruits = ["apple", "banana", "cherry", "banana"]

fruits.remove("banana")
# fruits is now ['apple', 'cherry', 'banana']

popped_fruit = fruits.pop(1) # 'cherry'
# fruits is now ['apple', 'banana']

del fruits[0]
# fruits is now ['banana']

fruits.clear()
# fruits is now []
```

### ⚙️ 1.4 Useful List Methods

Here are some other common and useful methods.

| Method | Description |
| --- | --- |
| `len(list)` | Returns the number of elements in the list. |
| `sort()` | Sorts the list in ascending order (in-place). |
| `sorted(list)` | Returns a **new** sorted list without modifying the original. |
| `reverse()` | Reverses the elements of the list (in-place). |
| `count(item)` | Returns the number of times a specified element appears. |
| `index(item)` | Returns the index of the first occurrence of a specified value. |

### 🚀 1.5 List Comprehensions

A concise and elegant way to create lists. It's often more readable and faster than using traditional loops.

```python
# Create a list of squares from 0 to 9
squares = [x**2 for x in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Create a list of even numbers from another list
numbers = [1, 2, 3, 4, 5, 6]
evens = [x for x in numbers if x % 2 == 0]
# [2, 4, 6]
```

---

## 📖 Chapter 2: Unlocking Dictionaries

Dictionaries are used to store data values in **key:value** pairs. They are **ordered** (as of Python 3.7), **mutable**, and do **not allow duplicate keys**.

### ✨ 2.1 Creating Dictionaries

Create a dictionary by placing key-value pairs inside curly braces `{}`, separated by commas.

```python
# An empty dictionary
empty_dict = {}

# A simple dictionary
person = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}

# Using the dict() constructor
person2 = dict(name="Jane Doe", age=25, city="London")
```

> **💡 Pro-Tip:** Keys must be of an immutable type (like strings, numbers, or tuples). Values can be of any data type.

### ⛓️ 2.2 Accessing and Modifying Items

You can access dictionary items by referring to their key name, inside square brackets `[]`.

```python
person = {"name": "John Doe", "age": 30}

# Accessing a value
print(person["name"])  # Output: John Doe

# Using the get() method is safer
print(person.get("age")) # Output: 30
print(person.get("country")) # Output: None (avoids KeyError)

# Adding a new key-value pair
person["email"] = "john.doe@example.com"
# person is now {'name': 'John Doe', 'age': 30, 'email': 'john.doe@example.com'}

# Modifying a value
person["age"] = 31
# person is now {'name': 'John Doe', 'age': 31, 'email': 'john.doe@example.com'}
```

### 🛠️ 2.3 Removing Items

There are several methods to remove items from a dictionary.

- `pop()`: Removes the item with the specified key name.
- `popitem()`: Removes the last inserted item (in Python 3.7+).
- `clear()`: Empties the dictionary.
- `del`: A keyword to remove an item with a specified key.

```python
person = {"name": "John Doe", "age": 30, "city": "New York"}

person.pop("age")
# person is now {'name': 'John Doe', 'city': 'New York'}

person.popitem()
# person is now {'name': 'John Doe'}

del person["name"]
# person is now {}

person.clear()
# person is now {}
```

### ⚙️ 2.4 Useful Dictionary Methods & Iteration

Here are some common methods for working with dictionaries.

| Method | Description |
| --- | --- |
| `keys()` | Returns a view object displaying a list of all the keys. |
| `values()` | Returns a view object displaying a list of all the values. |
| `items()` | Returns a view object displaying a list of key-value tuple pairs. |
| `update(dict2)` | Updates the dictionary with items from another dictionary. |

You can iterate through dictionaries easily.

```python
person = {"name": "John", "age": 30, "city": "New York"}

# Iterate over keys
for key in person.keys():
    print(key)

# Iterate over values
for value in person.values():
    print(value)

# Iterate over key-value pairs
for key, value in person.items():
    print(f"{key}: {value}")
```

### 🚀 2.5 Dictionary Comprehensions

Similar to list comprehensions, dictionary comprehensions provide a concise way to create dictionaries.

```python
# Create a dictionary of squares
squares = {x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Create a dictionary from two lists
keys = ['a', 'b', 'c']
values = [1, 2, 3]
my_dict = {k: v for (k, v) in zip(keys, values)}
# {'a': 1, 'b': 2, 'c': 3}
```
