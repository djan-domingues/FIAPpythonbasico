minutos = int(input("Digite os minutos que sua máquina esta marcando no momento: "))
fatorial = 1

while(minutos > 1):
    fatorial *= minutos
    minutos -= 1

print(f"A senha que você deve utilizar é: LIBERDADE{fatorial}")

