def palchk(snt):
    lst = list(snt)
    if lst[0] == lst[-1]:
        lst.pop(0)
        lst.pop(-1)
    else:
        return "Not Palindrome"
    
    if len(lst) < 2:
        return "Palindrome"
    else:
        return palchk(lst)

sentence = input("Sentence: ")
sentence = sentence.lower()
print(palchk(sentence))