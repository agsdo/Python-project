# O comando print executá ações e recebe argumentos,
# exibindo no console o que está entre os () e/ou "".
print (12345)
print ('Alexsandro', 'Gilson') 
# Por padrão, ao inserir uma ',(espaço)', no console acrescentará um espaço entre os comandos. 
# O que seria a mesma coisa que:
print ('Alexsandro Gilson')
# Como esse comando, basicamente, recebe argumentos,
# pode receber 'argumentos nomeados', predefinidos, com funções diversas. Ex.:
# sep e end são argumentos da função print que representam respectivamente "separador" e "fim".
print ('Alexsandro', 'Gilson', sep='-') # o argumento 'SEP' me permite definir um tipo de separador a ser utilizado.
# Neste exemplo, no lugar de separar os nomes com o espaço, utilizará um -. 
# O comando PRINT naturalmente vem com uma quebra de linha, ou seja, após o comando o cursor passará para a linha seguinte.
# Podemos contornar isso com o argumento end=' '. O comando end, também, já é naturalmente dotado de quebra de linha
# mas, se atribuirmos o valor "nada" a ele, não teremos a quebra. Vejamos:
print ('Alexsandro', 'Gilson', sep='-', end='')
print ('João', 'e', 'Maria', sep='-', end='') # Assim, teremos tudo executado na mesma linha.
# Vale ressaltar que podemos atribuir qualquer coisa ao end, que será mostrado ao final da linha. 
# O python também diferencia letras maiúsculas de minúsculas, então, comandos sempre em letras minúsculas.  
#Print ('asdf') - Digitado dessa forma, teríamos um erro, exceto se definido antes.  