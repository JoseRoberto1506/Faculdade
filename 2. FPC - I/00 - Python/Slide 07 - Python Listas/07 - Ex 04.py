from random import randint
idades = [randint(1, 100) for i in range(20)]
print(idades)
print(f"A maior idade é {max(idades)}")
print(f"A menor idade é {min(idades)}")
