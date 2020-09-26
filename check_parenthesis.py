def areParanthesisBalanced(expr):
    stack = []
    for char in expr:
        if char in ["[", "(", "{"]:
            stack.append(char)
        else:
            if not stack:
                return False
            curr_char = stack.pop()
            if curr_char == '(':
                if char != ')':
                    return False

            if curr_char == '[':
                if char != ']':
                    return False

            if curr_char == '{':
                if char != '}':
                    return False

    if stack:                     # check if stack is not empty
        return False
    return True


if areParanthesisBalanced("()("):
    print('Balan')
else:
    print("Unbalan")
    
   # Hi from github!!
