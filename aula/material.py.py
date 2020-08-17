#calculo de material usado na reforma da casa
comprimento = float(input("digite o quantos metros  a sala tem: "))
altura = float(input("digite a quantidade de tinta usado nas paredes: "))
largura = float(input("digite o volume da sala: "))
area_sala = largura * comprimento
volume_da_sala = largura * comprimento * altura
area_das_paredes_da_sala =  2 * altura * largura + 2 * altura * comprimento
print("a quantidade de piso da sala é:{}".format(area_sala))
print("a quantida de tinta na sala é:{}".format(volume_da_sala))
print("volume em metros cubicos para estima a potencia do arcondicionado e:{}".format(area_das_paredes_da_sala))
