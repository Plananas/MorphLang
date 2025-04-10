# MorphLang
An interpreted programming language using syntax from multiple languages, much like Pseudocode

---

## Overview

This language supports:

- Arithmetic and Boolean Operations
- If and While
- Functions
- User input/output
- Inline Comments
- Integers, Floats, and Strings

---

## How To Run
- Python 3.10 must be installed
- Run `python Morphlang.py <filename.morph>`

---

## **Tokens and Syntax**

### **Literals**

| Type    | Example                                 |
|---------|-----------------------------------------|
| Integer | `42`                                    |
| Float   | `4.2`                                   |
| String  | `'Hello'` or `"Hello"`                  |
| Boolean | `true` or `false` (not case sensitive)  |

---

### **Arithmetic Operators**

| Symbol | Meaning        |
|--------|----------------|
| `+`    | Addition       |
| `-`    | Subtraction    |
| `*`    | Multiplication |
| `/`    | Division       |

---

### **Boolean Operators**

| Symbol          | Meaning               |
|-----------------|-----------------------|
| `==`            | Equal                 |
| `!=`            | Not equal             |
| `<`             | Less than             |
| `>`             | Greater than          |
| `<=`            | Less than or equal    |
| `>=`            | Greater than or equal |
| `!`             | Not                   |
| `&&` / `&`      | And                   |
| `\|` or `\|\|`  | OR                    |

---

### **Assignment**

```plaintext
x = "Hello
y = "World"
```

Assigns "Hello" to the variable x and "World" to the variable y

- Must start with a letter
- Can include letters, digits, and underscores

---

### **Keywords**

| Keyword             | Meaning                     |
|---------------------|-----------------------------|
| `print`             | Output to the console       |
| `ask`               | Input from the user         |
| `if`                | Start if statement          |
| `then`              | Follow up after a condition |
| `else`              | Alternative condition block |
| `endif`             | End of if statement         |
| `while`             | Start a while loop          |
| `endwhile`          | End a while loop            |
| `function` or `def` | Define a function           |
| `return`            | Return from a function      |

---

### **Control Flow**

**If Statements**
```plaintext
if x > 10 then 
    print "Hello"
else
    print "World"
endif
```
**While Loops**
```plaintext
while condition then
    # code
endwhile
```

### **Input/Output**

```plaintext
word = ask "Enter a word"
print "The word is: " + word

```

### **Functions**

```plaintext
function greeting(name) {
    print hello() + name
}

def hello() {
    return "Hello"   
}

```

### **Comments**

Start the comment with `#`. Everything after will be ignored

Do not end a file with a comment

```plaintext
# This is a comment
```


## Further Development

- More Keyword (e.g. 'for', 'break')
- Larger variety of language syntax
