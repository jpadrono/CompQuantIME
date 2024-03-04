
i = 1j

print(i**2, i**3, i**4, i**5)

# vemos que o padrão se repete com mod 4

p = int(input("escolha a potência de i que será claculada: "))

if p % 4 == 0:
  print("o resultado da potência é 1")
elif p % 4 == 1:
  print("o resultado da potência é i")
elif p % 4 == 2:
    print("o resultado da potência é -1")
else:
    print("o resultado da potência é -i")