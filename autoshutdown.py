import os

shutdown = input("Do you wish to shutdown your computer ? (yes / no): ")

if shutdown == 'yes':
    print("===============================")
    print("[0} - Shutdown agora")
    print("[1] - Shutdown daqui a 1 Hora")
    print("[2] - Shutdown daqui a 2 Horas")
    print("[3] - Shutdown daqui a 3 Horas")
    print("[4] - Shutdown daqui a 4 Horas")
    print("[5] - Shutdown daqui a 5 Horas")
    print("===============================")
    print()
    resposta = int(input())
    if resposta == 0:
        os.system("shutdown /s /t 1")
    if resposta == 1:
        os.system("shutdown /s /t 3600")
    if resposta == 2:
        os.system("shutdown /s /t 7200")
    if resposta == 3:
        os.system("shutdown /s /t 10800")
    if resposta == 4:
        os.system("shutdown /s /t 14400")
    if resposta == 5:
        os.system("shutdown /s /t 18000")
if shutdown == 'no':
    exit()
