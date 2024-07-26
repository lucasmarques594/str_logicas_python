"""
Estrutturas condicionais
if, else, elif

"""

idade = 18

if idade <18: #Estrutura que responde de acordo com o parametro descrito
    print(f'menor de idade') 
elif idade == 18: #É um parametro sendo já um IfElse pulando as etapas anteriores se a resposta for a que tiver descrito no parametro 
     print(f'tem {idade} anos')
else:   #Caso não for de acordo com o parametro essa vai ser a 'segunda' resposta
     print(f'maior de idade')
       