def chkprrec(num, chk = 2):
    if num == 2:
        return True
    elif num % chk == 0 or num == 1:
        return False
    elif int(num**0.5)+1 == chk:
        return True
    else:
        return chkprrec(num, chk+1)

n = int(input("Number: "))
print(chkprrec(n))