
#Merge Sort

import random
def mergesort(lst):
    if len(lst)>1:
        mid = len(lst)//2
        left_half = lst[:mid]
        right_half = lst[mid:]
        mergesort(left_half)
        mergesort(right_half)
        i = j = k = 0
        while i<len(left_half) and j<len(right_half):
            if left_half[i] < right_half[j]:
                lst[k] = left_half[i]
                i += 1
            else:
                lst[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            lst[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            lst[k] = right_half[j]
            j += 1
            k += 1
        return lst
    
list_num = []
for i in range(10):
     list_num.append(random.randint(0,999))
print("Unsorted List")
print(list_num)
print("Sorted List")
print(mergesort(list_num))
