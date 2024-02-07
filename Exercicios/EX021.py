import time

timer = 11
for x in range(0, 10):
    timer = timer - 1
    print(timer)
    time.sleep(1)
    if timer == 1:
        print("Feliz Ano Novo!!!")
