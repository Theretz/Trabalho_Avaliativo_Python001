#Input de dados
HNOR = float(input('Digite a quantidade de horas trabalhadas pelo funcionário: '))
HEX = float(input('Digite a quantidade de horas extras trabalhadas pelo funcionário: '))
HE = float(input('Digite o adicional pela(s) hora(s) extra(s) trabalhada(s) pelo funcionário: '))
VH = float(input('Digite o valor pago por hora v/h: '))
Des_Percentual = float(input('Digite o percentual de desconto aplicado ao salário bruto: '))
nome = str(input('Digite o nome completo do funcionário: ').upper())
CPF = str(input('Digite o CPF do funcionário: ').upper())
cargo = str(input('Digite o cargo do funcionário: ').upper())

#Processamento de dados
Sal_Bruto = HNOR + HEX
DES = Sal_Bruto * (Des_Percentual / 100)
Sal_liq = Sal_Bruto - DES  

#Output de dados
print("\nRECIBO DE PAGAMENTO")
print(f'Nome: {nome}')
print(f'CPF: {CPF}')
print(f'Cargo: {cargo}')
print(f'Salário Bruto: {Sal_Bruto}')
print(f'Desconto do Salário: {DES}')
print(f'Salário Final: \\033[1m{Sal_liq}\\033[m')