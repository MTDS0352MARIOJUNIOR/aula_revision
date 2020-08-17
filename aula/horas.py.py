#horas que se passaram
hora = float(input("digite as horas: "))
minutos = float(input("digite os minutos: "))
segundo = float(input("digite os segundos: "))
horas = hora * 60 *60
minutos = minutos * 60
segundos = 1/60
resultado = horas * minutos * segundos
print("se passaram no total desde a ultima meia-hora, segundo:{}".format(resultado))
