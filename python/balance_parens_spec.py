from balance_parens import balance_parens

# Add more test cases!...
print(balance_parens("abc(d)e(fgh))(i)j)k") == "abc(d)e(fgh)(i)jk")
print(balance_parens("abc((d)e(fgh)(i)j(k") == "abc(d)e(fgh)(i)jk")

# Challenge: nested parentheses...
print(balance_parens("abc(d)(ef(g(h))ij)k)lm()o)p") == "abc(d)(ef(g(h))ij)klm()op")