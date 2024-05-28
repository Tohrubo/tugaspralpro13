def comb(n, r):
    if r == 0 or n == r:
        return 1
    else:
        return comb(n-1, r-1) + comb(n-1, r)

num = int(input("n = "))
rr = int(input("r = "))
print(comb(num, rr))