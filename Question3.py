def oddco(num, chk = 1, sc = 2):
    if num == 0:
        return 0
    elif num == 1:
        return chk
    else:
        return chk + oddco(num-1, chk + sc, sc*2)

n = int(input("To n = "))
print(oddco(n))