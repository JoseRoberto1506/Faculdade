# Para realizar testes diferentes, mudar os valores dos parâmetros nas chamadas das funções

def fatorial(n):
  if n < 0:
    return 0
  elif n == 0:
    return 1
  else:
    return n * fatorial(n - 1)

print(f'Fatorial: {fatorial(5)}')


def exponencial(a, n):
  # Exceção
  if (a == 0) and (n == 0):
    return "Não pode ser calculado"
  # Caso base
  elif n == 0:
    return 1
  # Cálculo recursivo
  else:
    return a * exponencial(a, n-1)

print(f'Exponencial: {exponencial(2, 3)}')


def expmod(a, n, m):
  # Caso base
  if a == 0 and n == 0:
    return "Impossível calcular"
  elif m < 2:
    return "Impossível calcular"
  elif n == 0:
    return 1
  # Cálculo recursivo
  elif n % 2 == 0:
    return expmod(a, n/2, m)**2 % m
  else:
    return ((expmod(a, n/2 - 0.5, m)**2 % m) * (a % m)) % m

print(f'Exponencial modular: {expmod(-2, 4, 8)}')


def mdc(a, b):
  if a < b:
    a, b = b, a
  # Caso base
  if a == 0 and b == 0:
    return "Indeterminado"
  elif b == 0:
    return a  
  # Cálculo recursivo
  else:
    return mdc(b, a % b)

print(f'MDC: {mdc(98, 66)}')
