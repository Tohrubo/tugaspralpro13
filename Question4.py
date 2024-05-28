def numsum(num):
    lst = list(num)
    if len(lst) < 1:
        return 0
    else:
        n = int(lst[0])
        lst.pop(0)
        return n + numsum(lst)

n = input("Numbers: ")
print(numsum(n))