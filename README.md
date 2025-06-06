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

This concludes our initial chapter on lists. Let me know what topic you'd like to cover next! We can dive into Tuples, Dictionaries, Sets, or other advanced features. 
