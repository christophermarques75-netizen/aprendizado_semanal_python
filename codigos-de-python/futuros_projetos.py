user = int(input("valor inicial do investimento:  "))
investimento_mensal = int(input("valor investimento mensalmente: "))
imposto_memsal = 0.019
tempo = int(input("valor em meses: "))

for tempo in range(1, tempo + 1):
    user += investimento_mensal
    user = user * (1 + imposto_memsal)

diferença = user - investimento_mensal

print(f'{diferença:.2f}')
print(f"{user:.2f}")