def isValidParentheses(s: str) -> bool:
    # Declare an empty stack
    stack = []

    # Map closing with it's opening brackets in a dictionary
    closeToOpen = {")" : "(", "]": "[", "}" : "{"}

    # For every character 'c' in s,
    for c in s:
        # If it is a closing bracket
        if c in closeToOpen:
            # Check if stack is not empty and it's top matches corresponding opening bracket
            if stack and stack[-1] == closeToOpen[c]:
                # If yes, then pop from stack
                stack.pop()
            else:
                # If no, then return false
                return False
        else:
            # If it is an opening bracket, push into the stack
            stack.append(c)

    # If the stack is empty return True, else return False
    return True if not stack else False

def main():
    s = "({})"
    print(f"Input: {s}")

    res = isValidParentheses(s)
    print(f"Output: {res}")

if __name__ == "__main__":
    main()