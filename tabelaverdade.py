a = 2
b = 6
c = 3

operacaoAnd1 = a == b and c * a == b
print("1:", operacaoAnd1)

operacaoOr1 = a == b or c * a == b
print("1:", operacaoOr1)

operacaoAnd2 = a == c + b and c == b
print("2:", operacaoAnd2)

operacaoOr2 = a == c + b or c == b
print("2:", operacaoOr2)

operacaoAnd3 = a > 5 and b > 3
print("3:", operacaoAnd3)

operacaoOr3 = a > 5 or b > 3
print("3:", operacaoOr3)

operacaoAnd4 = a < 5 and c >= 3
print("4:", operacaoAnd4)

operacaoOr4 = a < 5 or c >= 3
print("4:", operacaoOr4)

operacaoAnd5 = not b == 6 and 3 * 2 == b
print("5:", operacaoAnd5)

operacaoOr5 = not b == 6 or 3 * 2 == b
print("5:", operacaoOr5)

operacaoAnd6 = c < 5 and not b > 6
print("6:", operacaoAnd6)

operacaoOr6 = c < 5 or not b > 6
print("6:", operacaoOr6)