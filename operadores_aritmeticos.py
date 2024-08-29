a = 5
b = 3
c = 4

# adição
resultado = a + b + c
print(f"soma:{resultado}")

# subtração
resultado = c - b
print(f"subtracao: {resultado}")

# multiplicação
resultado = b * a
print(f"multiplicacao: {resultado}")

# divisão
resultado = a / b
print(f"divisao: {resultado}")

# divisao inteira
resultado = a // b
print(f"divisao inteira: {resultado}")

# resto da divisao
resultado = a % b
print(f"resto da divisao: {resultado}")

#exponencial
resultado = a ** b
print(f"exponencial: {resultado}")


saldoinicial = 50
custorefrigerante = 8
custopao = 4
customortadela = 39.90

valorcompra = (custorefrigerante * 2) + custopao + ((customortadela / 1000) * 300)
saldofinal = saldoinicial - valorcompra
print(f"Jose tinha {saldoinicial} e ficou com {saldofinal}")

