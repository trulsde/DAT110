import math

def pdf(x, l):

    return math.exp(-l) * l**x / math.factorial(x)

# 2.3
l = 75
sum = 0
for i in range(61):
    sum = sum + pdf(i, l)
    print(pdf(i, l))

print(sum)

# 2.4

print(f'Probability for serving exactly 70 customers: {pdf(70, l) * 100:.2f}%')