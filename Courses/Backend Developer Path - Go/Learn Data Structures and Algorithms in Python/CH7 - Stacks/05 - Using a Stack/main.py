from stack import Stack

def is_balanced(parentheses: str) -> bool:
    open_parentheses = Stack()

    for parenthesis in parentheses:
        if parenthesis == '(': open_parentheses.push('(')

        elif parenthesis == ')':
            if open_parentheses.size() == 0: return False
            open_parentheses.pop()

    return open_parentheses.size() == 0
