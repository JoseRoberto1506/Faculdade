while True:
    alunos = int(input())
    if 1 <= alunos <= 50:
        break
while True:
    monitores = int(input())
    if 1 <= monitores <= 50:
        break

if alunos + monitores <= 50:
    print('S')
else:
    print('N')
