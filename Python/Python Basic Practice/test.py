x = 1534236469
a = 0
neg = False
maxNeg = 2**31
maxPos = maxNeg - 1
if x < 0:
    x *= -1
    neg = True

while x != 0:
    a = x % 10 + a * 10
    if (neg == True and a > maxNeg) | (neg == False and a > maxPos):
        a = 0
    x = int(x/10) 
if neg == True:
    a = -1*a
print (a)