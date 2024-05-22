# Operaciones a nivel de bits en Python

# Definir dos números enteros
num1 = 10    # Representación binaria: 1010
num2 = 7     # Representación binaria: 0111

# Operador AND a nivel de bits (&)
resultado_and = num1 & num2
print("AND a nivel de bits:", resultado_and)

# Operador OR a nivel de bits (|)
resultado_or = num1 | num2
print("OR a nivel de bits:", resultado_or)

# Operador XOR a nivel de bits (^)
resultado_xor = num1 ^ num2
print("XOR a nivel de bits:", resultado_xor)

# Operador NOT a nivel de bits (~)
resultado_not_num1 = ~num1
print("NOT a nivel de bits para num1:", resultado_not_num1)

# Desplazamiento a la izquierda (<<)
resultado_left_shift = num1 << 1
print("Desplazamiento a la izquierda:", resultado_left_shift)

# Desplazamiento a la derecha (>>)
resultado_right_shift = num1 >> 1
print("Desplazamiento a la derecha:", resultado_right_shift)
