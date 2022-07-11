def esPrimo(num):
    for x in range(2, num):
        if num % x == 0:
            print("No es primo", x, "es divisor")
            return False
    print("Es primo")
    return True

esPrimo(5)
esPrimo(25)
esPrimo(3)
esPrimo(4)
esPrimo(9)
esPrimo(90)
esPrimo(59)