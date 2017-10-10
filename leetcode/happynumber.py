def isHappy(n):
    number = str(n)
    total = 0
    for i in range(0,len(number)):
        total += i^2

    if total == 1:
        return True
    else:
        return self.isHappy(total)




print isHappy(1234)
