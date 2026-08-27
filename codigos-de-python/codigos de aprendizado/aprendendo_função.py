def calcular_imposto(salario):
    salario = float(salario)
    if salario <= 1518:
        imposto_atual = 0.075
        desconto =  salario * imposto_atual
        valor_descontato = salario + desconto 
        imposto_atual = imposto_atual * 100

    elif salario > 1518 and salario < 2793.88:
        imposto_atual = 0.09
        desconto =  salario * imposto_atual
        valor_descontato = salario + desconto 
        imposto_atual = imposto_atual * 100

    elif salario > 2793.89 and salario < 4190.83:
        imposto_atual = 0.12
        desconto =  salario * imposto_atual
        valor_descontato = salario + desconto 
        imposto_atual = imposto_atual * 100
    
    elif salario > 4190.84 and salario < 8157.41:
        imposto_atual = 0.14
        desconto =  salario * 0.14
        valor_descontato = salario + desconto 
        imposto_atual = imposto_atual * 100
    
    return valor_descontato, imposto_atual

user = input("qual o valor do seu salario: ")

try:
    salario_num = float(user.replace(",", "."))
    desconto = calcular_imposto(user)[0]
    imposto = calcular_imposto(user)[1]
    print(f"seu salario seria {desconto} sem o imposto de {imposto:.1f}% do governo")


except ValueError:
    print("Somente valores numéricos, bro.")


    