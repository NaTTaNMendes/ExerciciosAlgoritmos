i = 1
while i <= 10:
    if (i == 1):
        print("      1     2     3     4     5     6     7     8     9     10")
    j = 1
    while (j <= 10):
        if (j == 1):
            if(i == 10):
                print(i,"   ", end="")  
            else: 
                print(i,"    ", end="")
        if (i * j < 10):
            print(i * j, "    ", end="")
        else:
            print(i * j, "   ", end="")
        j += 1
    i += 1
    print()