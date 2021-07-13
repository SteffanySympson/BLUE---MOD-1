print ("Bem Vindo!")
print ()

sexo = input ("Informe seu sexo biológico no formato F ou M: ").upper()

while (sexo != "F" and sexo != "M"):
  print ("Entrada não aceita, tente novamente. ")
  sexo = input ("Informe seu sexo biológico no formato F ou M: ").upper()
else:  
  print ("Obrigada pela participação!")