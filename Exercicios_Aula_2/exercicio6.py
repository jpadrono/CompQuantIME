str1 = input("Digite o primeiro complexo no formato a+bj: ")
str2 = input("Digite o segundo complexo no formato a+bj: ")

c1 = complex(str1)
c2 = complex(str2)
tol = 10e-5

# uso da tolerância devido ao erro associado a operaçoes com pontos flutuantes
print("teste a:")
print("|c1|*|c2| = |c1*c2|", (abs(c1)*abs(c2) - abs(c1*c2) < tol))

print("teste b:")
print("|c1+c2| <= |c1|+|c2|", (abs(c1+c2) <= abs(c1)+abs(c2)))