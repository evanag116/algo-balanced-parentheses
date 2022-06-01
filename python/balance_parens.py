def balance_parens(str):
    stack = []
    symbols = {"(":")", ")":"(", "[":"]", "]":"[", "{":"}", "}":"{"}
    ans = ""
    indices = []

    
    for i, char in enumerate(str):
        if char.isalnum():
            indices.append(i)
            continue
        elif stack and char in symbols:
            if stack[-1] == symbols[char]:
                stack.pop()
                indices.pop()
            else:
                stack.append(char)
                indices.append(i)
        else:
            stack.append(char)
            indices.append(i)
        # print(stack)

    for i in range(len(str)):
        if i not in indices:
            ans += str[i]
    
    
    return stack

print(balance_parens(")("))
    

# print(balance_parens("(()a))"))
# print(balance_parens("(()()("))
# print(balance_parens("abc(d)e(fgh))(i)j)k"))

