# 🧮 Calculator App

A powerful command-line calculator that evaluates mathematical expressions with proper operator precedence! ✨

## 🚀 Getting Started

### 📋 Prerequisites
- Python 3.10+ 🐍

### ▶️ Running the Calculator

Execute the calculator from the command line with a mathematical expression:

```bash
python main.py "<expression>"
```

### 💡 Usage Examples

```bash
# Basic arithmetic ➕➖✖️➗
python main.py "3 + 5"
python main.py "10 - 4"
python main.py "3 * 4"
python main.py "10 / 2"

# Advanced operations 🔢
python main.py "7 // 2"      # Floor division
python main.py "7 % 3"       # Modulo
python main.py "2 ** 3"      # Exponentiation

# Complex expressions 🎯
python main.py "2 * 3 - 8 / 2 + 5"
python main.py "3 * 4 + 5"
```

### 📤 Output Format

The calculator returns results in JSON format:

```json
{
  "expression": "3 + 5",
  "result": 8
}
```

## 🎯 Supported Operations

| Operator | Name | Description |
|----------|------|-------------|
| `+` | Addition | Adds two numbers ➕ |
| `-` | Subtraction | Subtracts two numbers ➖ |
| `*` | Multiplication | Multiplies two numbers ✖️ |
| `/` | Division | Divides two numbers ➗ |
| `//` | Floor Division | Integer division 🔢 |
| `%` | Modulo | Remainder operation 🔁 |
| `**` | Exponentiation | Power operation ⬆️ |

## ⚙️ Algorithm Breakdown

The calculator uses the **Shunting Yard Algorithm** approach with two stacks to evaluate expressions with proper operator precedence. Here's how it works:

### 🏗️ Architecture

```
Expression String → Tokenizer → Evaluator → Result
```

### 📊 Step-by-Step Process

#### 1️⃣ Tokenization 🔤
The input expression is split into tokens (numbers and operators) by whitespace:
```
"2 * 3 - 8 / 2 + 5" → ["2", "*", "3", "-", "8", "/", "2", "+", "5"]
```

#### 2️⃣ Two-Stack Evaluation 🤝
The algorithm uses two stacks:
- **Operator Stack** (`ops`): Stores operators temporarily
- **Value Stack** (`vals`): Stores numeric values

#### 3️⃣ Operator Precedence Rules ⚖️
Operators are processed according to their precedence levels:

| Precedence | Operators |
|------------|-----------|
| 3 (Highest) | `**` (Exponentiation) |
| 2 | `*`, `/`, `//`, `%` |
| 1 (Lowest) | `+`, `-` |

#### 4️⃣ Processing Logic 🔄

For each token in the expression:

1. **If it's a number** 🔢:
   - Convert to float and push onto the value stack

2. **If it's an operator** ⚙️:
   - While the operator stack is not empty AND the top operator has higher or equal precedence:
     - Pop the operator and apply it to the top two values
   - Push the current operator onto the operator stack

3. **After all tokens are processed** 🏁:
   - Apply all remaining operators in the stack

#### 5️⃣ Applying Operators 🎯
When applying an operator:
1. Pop the operator from the operator stack
2. Pop two values from the value stack (b first, then a)
3. Compute `a operator b`
4. Push the result back onto the value stack

### 🧮 Example Walkthrough

Let's trace through `"2 + 3 ** 2"`:

| Step | Token | Action | Ops Stack | Values Stack |
|------|-------|--------|-----------|--------------|
| 1 | `2` | Push value | `[]` | `[2]` |
| 2 | `+` | Push operator | `[+]` | `[2]` |
| 3 | `3` | Push value | `[+]` | `[2, 3]` |
| 4 | `**` | Higher precedence than `+`, push | `[+, **]` | `[2, 3]` |
| 5 | `2` | Push value | `[+, **]` | `[2, 3, 2]` |
| 6 | End | Apply `**` → 3**2=9 | `[+]` | `[2, 9]` |
| 7 | End | Apply `+` → 2+9=11 | `[]` | `[11]` |

**Result: 11** ✅

### 🛡️ Special Cases Handled

- **Division by zero** ➗0: Returns `inf` (infinity) or `nan` (not a number)
- **Zero to negative power** 0⁻²: Safely returns `inf`
- **Empty expressions** 🕳️: Returns `None`
- **Invalid tokens** ❌: Raises `ValueError`
- **Insufficient operands** 🔢: Raises `ValueError`

## 🧪 Testing

Run the test suite to verify all functionality:

```bash
python tests.py
```

The test suite covers:
- ✅ Basic arithmetic operations
- ✅ Operator precedence
- ✅ Edge cases (division by zero, etc.)
- ✅ Error handling
- ✅ Complex nested expressions

## 📁 Project Structure

```
calculator/
├── main.py          # CLI entry point 🚪
├── tests.py         # Test suite 🧪
├── README.md        # This file 📖
└── pkg/
    └── calculator.py # Core calculator logic 🧮
```

## 🤝 Contributing

Contributions are welcome! Feel free to:
- 🐛 Report bugs
- ✨ Add new features
- 📚 Improve documentation
- 🧪 Add more test cases

---

Made with ❤️ and Python 🐍
