import matplotlib.pyplot as plt
import random as rand
import time

def quick_sort(arr):
    if len(arr) < 2:
        return arr
    pivot = rand.choice(arr)
    left = list(filter(lambda it: it < pivot, arr))
    right = list(filter(lambda it: it > pivot, arr))
    return quick_sort(left) + [pivot] + quick_sort(right)


def merge(left, right):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged += left[i:]
    merged += right[j:]
    return merged

def merge_sort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

test1: list[int] = [rand.randint(-100, 100) for _ in range(100)]
test2: list[int] = [rand.randint(-1000, 1000) for _ in range(1000)]
test3: list[int] = [rand.randint(-10000, 10000) for _ in range(10000)]
test4: list[int] = [rand.randint(-100000, 100000) for _ in range(100000)]
test5: list[int] = [rand.randint(-1000000, 1000000) for _ in range(1000000)]
test6: list[int] = [rand.randint(-10000000, 10000000) for _ in range(10000000)]

t1 = time.time()
res_q1 = quick_sort(test1.copy())
t2 = time.time()
res_m1 = merge_sort(test1.copy())
t3 = time.time()
res_q2 = quick_sort(test2.copy())
t4 = time.time()
res_m2 = merge_sort(test2.copy())
t5 = time.time()
res_q3 = quick_sort(test3.copy())
t6 = time.time()
res_m3 = merge_sort(test3.copy())
t7 = time.time()
res_q4 = quick_sort(test4.copy())
t8 = time.time()
res_m4 = merge_sort(test4.copy())
t9 = time.time()
res_q5 = quick_sort(test5.copy())
t10 = time.time()
res_m5 = merge_sort(test5.copy())
t11 = time.time()
res_q6 = quick_sort(test6.copy())
t12 = time.time()
res_m6 = merge_sort(test6.copy())
t13 = time.time()

x = [len(test1), len(test2), len(test3), len(test4), len(test5), len(test6)]

plt.plot(x, [t2 - t1, t4 - t3, t6 - t5, t8 - t7, t10 - t9, t12 - t11], label = 'Quick Sort')
plt.plot(x, [t3 - t2, t5 - t4, t7 - t6, t9 - t8, t11 - t10, t13 - t12], label = 'Merge Sort')
plt.xlabel('Размер массива')
plt.ylabel('Время, c')
plt.legend()
plt.show()