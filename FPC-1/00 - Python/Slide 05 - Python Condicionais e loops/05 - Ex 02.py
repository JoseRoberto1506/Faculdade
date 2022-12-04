temperatura = float(input("Temperatura (°C): "))

if temperatura >= 39:
    print("Febre alta")
elif 37 <= temperatura < 39:
    print("Febril")
else:
    print("Sem febre")
