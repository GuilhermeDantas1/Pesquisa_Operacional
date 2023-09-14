from pulp import *
     
#definir o tipo de problema
resultado = LpProblem('Produção_Monobloco',LpMinimize)
     
#definindo as variáveis do problema
x11 = LpVariable("x11", lowBound = 0)
x12 = LpVariable('x12', lowBound = 0)
x13 = LpVariable('x13', lowBound = 0)
x22 = LpVariable('x22', lowBound = 0)
x23 = LpVariable('x23', lowBound = 0)
x33 = LpVariable('x33', lowBound = 0)
   
#Resolvendo a função objetivo
resultado += 3000*x11 + 3200*x12 + 3400*x13 + 3000*x22 + 3200*x23 + 3200*x33
     
#definindo as restrições
resultado += x11 + x12 + x13 <= 2500 
resultado += x22 + x23 <= 2500
resultado += x33 <= 2000
resultado += x11 == 1000
resultado += x12 + x22 == 2000
resultado += x13 + x23 + x33 == 3000

#ver estrutura do problema
print(resultado)
     
# Função para resolver o problema
resultado.solve()
     
#Exibindo variaveis e seus valores encontrado pela solução
for v in resultado.variables():
  print (v.name, "=",v.varValue)
     
#Custo total calculado da função objetivo
print('custo total =',value(resultado.objective)) 