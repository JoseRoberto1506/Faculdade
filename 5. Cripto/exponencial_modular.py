def exponencial_modular(a, b, n):
  # Caso base
  if a == 0 and b == 0:
    return "Impossível calcular"
  elif n < 2:
    return "Impossível calcular"
  elif b == 0:
    return 1
  # Cálculo recursivo
  elif b % 2 == 0:
    return exponencial_modular(a, b/2, n)**2 % n
  else:
    return ((exponencial_modular(a, b/2 - 0.5, n)**2 % n) * (a % n)) % n


print(f'Exponencial modular: {exponencial_modular(5, 117, 7)}')
