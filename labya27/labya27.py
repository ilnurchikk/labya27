###########################1

from random import randint
# sum_negtiv = 0
# proiz = 0
# chet = 0
# nechet = 0
#
# a = [randint(-10, 10) for _ in range(10)]
# print(a)
# for i in a:
#     if i < 0:
#         sum_negtiv += i
# print(f" сумма негативных чисел:{i}")
# print()
# for j in a:
#     if (j % 2) == 0:
#         chet += j
#
# print(f"сумма четных чисел:{chet}")
# print()
# for m in a:
#     if (m % 2) != 0:
#         nechet += m
# print(f"сумма нечетных чисел:{nechet}")
# print()
# for n in a:
#     if n % 3 == 0:
#         proiz = n * proiz
# print(f"Произведение кратно 3: {proiz}")
# print()

##################1
# min_index = a.index(min(a))
# max_index = a.index(max(a))
# if min_index < max_index:
#     minmax = 1
#     for p in range(min_index + 1, max_index):
#         minmax *= a[p]
# else:
#     minmax = 1
#     for p in range(max_index + 1, min_index):
#         minmax *= a[p]
# print(f"произведение между min и max: {minmax}")
# print()
#
# polozhi = [v for v, x in enumerate(a) if x > 0]
# if len(polozhi) >= 2:
#     first_polozhi = polozhi[0]
#     last_polozhi = polozhi[-1]
#     if first_polozhi < last_polozhi:
#         sum_polozhi = sum(a[first_polozhi+1:last_polozhi])
#     else:
#         sum_polozhi = sum(a[first_polozhi+1:last_polozhi])
# else:
#     sum_polozhi = 0
# print(f"сумма между первым и последним положительным элементами:{sum_polozhi}")

################################2
chett = []
nechett = []
negativv = []
polozhit = []
b = [randint(-10, 10) for _ in range(10)]
print(b)
for u in b:
    if (u % 2) == 0:
        chett.append(u)
print(f" четные числа:{chett}")
print()
for q in b:
    if (q % 2) != 0:
        nechett.append(q)
print(f" нечетные числа:{nechett}")
print()

for y in b:
    if y < 0:
       negativv.append(y)
print(f"  негативные числа:{negativv}")
print()
for l in b:
    if l > 0:
       polozhit.append(l)
print(f"  положительные числа:{polozhit}")