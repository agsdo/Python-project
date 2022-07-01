#String - str: Tudo o que for colocado dentro de aspas. 

print('alguma coisa')#Pode ser entre aspas simples
print("Aspas duplas")#Ou entre aspas duplas.

#Caso eu precise colocar algum trexo ou palavra entre aspas dentro das aspas da str, 
#podemos iniciar o texto com um tipo de aspas e incluir o trexo entre aspas com outro tipo de aspas. 
#Além de outras formas que veremos adiante. 
#Ex.:
print("isso é uma 'string'(str)")
#Podemos usar também um caractere de escape:
print('isso é uma \'string\'(str)')#mas dessa forma fica feio. 

#Curiosidade: A \ é um caractere que o python interpreta, ex: \n - que significa quebra de linha. 
#Caso haja um \n no meio do código o texto será quebrado para a linha seguinte.
#Uma forma de evitar isso é colocar o 'r' na frente do texto, antes da primeira aspa.Ex.
print('alguma \n coisa')
print(r'alguma \n coisa')#O r a frente significa dizer para o interpretador que não queremos executar nada nessa linha. 
