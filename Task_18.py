A = [int(i) for i in input().split()]
n = len(A)
x = int(input())
diff = x
res = 0
for i in range (n):
    if abs(A[i] - x) < diff:
        res = A[i]
        diff =  abs(A[i] - x)
print(res)
