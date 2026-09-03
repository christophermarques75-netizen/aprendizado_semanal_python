def calcular_imposto(entrada2, label_resultado):
    try:
        salario = entrada2
        salario = float(salario.replace(",", "."))

        if salario <= 1621:
            imposto_atual = 0.075
            desconto =  salario * imposto_atual
            valor_descontato = salario + desconto 
            imposto_atual = imposto_atual * 100

        elif salario > 1621 and salario < 2902.84:
            imposto_atual = 0.09
            desconto =  salario * imposto_atual
            valor_descontato = salario + desconto 
            imposto_atual = imposto_atual * 100

        elif salario > 2902.84 and salario < 4354.27:
            imposto_atual = 0.12
            desconto =  salario * imposto_atual
            valor_descontato = salario + desconto 
            imposto_atual = imposto_atual * 100
        
        elif salario > 4354.27 and salario < 18157.41:
            imposto_atual = 0.14
            desconto =  salario * 0.14
            valor_descontato = salario + desconto 
            imposto_atual = imposto_atual * 100
        
        label_resultado.config(
            text=f"O valor do seu imposto(INSS) é R$ {desconto:.2f}\nsobre o seu salário liquido de R$ {salario:.2f}\npois desconta R${imposto_atual:.2f}% para o inss\n seu salario deveria ser {valor_descontato:.2f} bruto"
        )
    except ValueError:
        label_resultado.config(
            text="valor não aceito faz de novo"
        )

