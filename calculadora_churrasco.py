# crie um programa que calcule a quantidade de bebidas e de carne
# para a organização de um churrasco

# Etapas da resolução:
# 1) Solicitar o número de convidados
n_convidados = int(input('Digite o número de convidados: '))

# 2) Criar uma função para calcular a quantidade total de bebidas
def calcular_bebidas(convidados, consumo_por_pessoa_ml=800, volume_garrafa_litros=2.25):
    total_ml = convidados * consumo_por_pessoa_ml / 1000
    garrafas = int(total_ml // volume_garrafa_litros)
    if total_ml % volume_garrafa_litros > 0:
        garrafas += 1

    return garrafas

# 3) Criar uma função para calcular a quantidade total de carne
def calcular_carne(convidados, consumo_por_pessoa_grama=400):
    total_gramas = convidados * consumo_por_pessoa_grama
    total_kg = total_gramas / 1000
    return total_kg

# 4) Apresentar o resultado com os valores de total de carne e
# bebidas a serem comprados

garrafas = calcular_bebidas(n_convidados)
kg = calcular_carne(n_convidados)

print(f'n____Quantidade total para Churrasco_____')
print(f'Numero de convidados: {n_convidados}')
print(f'Garrafa(s) de 2,25L: {garrafas} garrafa(s)')
print(f'Carne necessária: {kg:.2f} kg')