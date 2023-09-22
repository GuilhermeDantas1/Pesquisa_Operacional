from pulp import *
     
#definir o tipo de problema
resultado = LpProblem('Dienta',LpMinimize)
     
#definindo as variáveis do problema
x1 = LpVariable("Arroz", lowBound = 0)
x2 = LpVariable('Ovos',  lowBound = 1)
x3 = LpVariable('Leite', upBound = 2, lowBound = 0)
x4 = LpVariable('Feijão', lowBound = 0)

#Resolvendo a função objetivo
resultado += 14*x1 + 13*x2 + 9*x3 + 19*x4
     
#definindo as restrições
resultado += 205*x1 + 160*x2 + 160*x3 + 260*x4 >= 2000 
resultado += 32*x1 + 13*x2 + 8*x3 + 14*x4 >= 65
resultado += 12*x1 + 54*x2 + 285*x3 + 80*x4 >= 800


#ver estrutura do problema
# print(resultado)
     
# Função para resolver o problema
resultado.solve()
     
#Exibindo variaveis e seus valores encontrado pela solução
for v in resultado.variables():
  print ('Porções de ', v.name, "=",f'{v.varValue:.2f}')
     
#Custo total calculado da função objetivo
print('\n custo total = ',f'{value(resultado.objective):.2f} Centavos') 

print('\n Consumo dos alimentos: \n')

for v in resultado.variables():
    arroz = v.varValue * 100
    ovos = v.varValue * 1
    leite = v.varValue * 237
    feijao = v.varValue * 260
    if (v.name == 'Arroz'):
        print(f'{arroz:.2f}', 'g de Arroz') 
    if (v.name == 'Ovos'):
        print(f'{ovos:.2f}', "unidades de ovos") 
    if (v.name == 'Leite'):
        print(f'{leite:.2f}', "ml de leite")
    if (v.name == 'Feijão'):
        print(f'{feijao:.2f}', "g de feijao")