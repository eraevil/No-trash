n,x = map(int,input().split())
price = []
for i in range(n):
    price.append(int(input()))

# print(n,x,price)

# n,x = 3,30
# price = [15,40,30]

# n,x = 4,100
# price = [20,90,60,60]

# n,x = 2,90
# price = [50,50]

# n,x = 5,100
# price = [10,20,30,40,52]

result = []
for m in range(2**n):
    b = [0]*n
    for i in range(0,n):
        b[i] = m % 2
        m = m // 2
    cost = 0
    for i in range(0,n):
        cost += price[i] * b[i]
    if cost >= x:
        result.append(cost)

min = 100000
for i in range(len(result)):
    if min > result[i]:
        min = result[i]

print(min)