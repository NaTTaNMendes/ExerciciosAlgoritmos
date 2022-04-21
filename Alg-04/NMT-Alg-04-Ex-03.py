print("-------------")
celsius = 0
while True:
    fahrenheit = (celsius*9/5) + 32
    print(" %.1f | %.1f " % (celsius, fahrenheit))
    celsius += 10
    if (celsius > 100):
        print("-------------")
        break
    else:
        print("------|------")