# n = int(input())
# arr = map(int,input().split())
# f,s=0,-101
# for i in arr:
#     if f<i:
#         f=i
#     elif i<=f:
#         if i>s and s!=f and i<f:
#             s=i
#     # print(f"F={f} S={s}")
# print(s)

n = int(input())
a = [int(x) for x in input().split()]
largest = secondlargest = -100
for x in a:
    if x > largest:
        secondlargest = largest
        largest = x
    elif x > secondlargest and x != largest:
        secondlargest = x
print(secondlargest)