# Balanced Parentheses

### Write an algorithm that takes in a string and returns a string with balanced parentheses only. The string will contain letters, numbers, and parentheses only.

```python
balanceParens("()") # should return "()"
balanceParens("a(b)c)") # should return "a(b)c"
balanceParens("(a)(bdd)c)") # should return "(a)(bdd)c"
balanceParens("a(dbvb)c)") # should return "a(dbvb)c"
balanceParens("a(b)(c)())") # should return "a(b)(c)()"
balanceParens(")(") # should return ""
balanceParens("(((((") # should return ""
balanceParens(")(())(") # should return "(())"
balanceParens("(()()(") # should return "()()"
balanceParens(")())(()()(") # should return "()()()"
```

### Challenge - Nested Parentheses
```python
balanceParens(")(())(")) # should return "(())"
```
