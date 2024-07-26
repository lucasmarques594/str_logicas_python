"""
Estruturas Lógicas: and(e) or(ou) not(não) is(é)

Operadores unários:
    - not, 
Operadores binários:
    - and, or , is
"""
#And = Precisa estarem com o valor de TRUE para ser validado o parametro no if
#Or = Precisa apenas um valor TRUE para ser validado e passar pelo parametro
#Not = Vai inverter o valor de FALSE para TRUE, vice-versa exemplo {if not ativo and logado} -> Nesse caso cairia no primeiro IF
#IS = O valor é comparado com um segund, Usamos para comparação 


ativo = True
logado = False

if ativo is logado: 
    print('Logado no sistema com sucesso')
else:
    print('Verifique se seu login está ativo')
