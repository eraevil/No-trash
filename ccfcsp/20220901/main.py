import math


# 接收输入
n, m = map(int, input().split())
a = list(map(int, input().split()))
# n,m = 7,23333
# a = [3,5,20,10,4,3,10]
#
# n,m = 15,32767
# a = [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
#
# n, m = 4,0
# a = [2,3,2,5]

# c 0,1,2,3,4,5,6,7
c = []
for i in range(int(n)+1):
    if i == 0:
        c.append(1)
    else:
        c.append(c[i-1] * int(a[i-1]))
# print("c  ",c)

# m % c 0,1,2,3,4,5,6,7
m_c = [0]
for i in range(1,n+1):
    m_c.append(m % c[i])
# print("m_c",m_c)

# b
b = [0]
for i in range(1,n+1):
    if i == 1:
        b.append(math.floor(m_c[i] / c[0]))
    else:
        b.append(math.floor((m_c[i] - b[i-1]) / c[i-1]))

# print(n,m)
# print('a',a)
# print('c',c)
# print('m_c',m_c)
# print('b',b[1:])
print(*b[1:])

# if __name__ == "__main__":