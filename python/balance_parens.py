def balance_parens(str):
    stack = []

    for i in range(len(str)):
        if str[i].isalpha():
            stack.append(str[i])
        else:
            if str[i] == "(":
                if ")" in str[i+1:]:
                    stack.append(str[i])
            else:
                if stack.count("(") > stack.count(")"):
                    stack.append(str[i])

    return "".join(stack)
        


