import math


def merge_sort(array, p, r):
    if p < r:
        q = math.floor((p+r)/2)

        merge_sort(array,p,q)
        merge_sort(array,q+1,r)
        merge(array,p,q,r)

    return array

def merge(array,p,q,r):
    n1 = q - p + 1
    n2 = r - q

    L = [0] * (n1 + 1)
    R = [0] * (n2 + 1)

    for i in range(n1):
        L[i] = array[p+i]

    for j in range(n2):
        R[j] = array[q+j+1]

    L[n1] = R[n2] = 10**9

    i = j = 0

    for k in range(p, r+1):
        if L[i] <= R[j]:
            array[k] = L[i]
            i = i + 1
        else:
            array[k] = R[j]
            j = j + 1




array1 = [42, 7, 89, 16, 73, 58, 31, 94, 12, 65]
print(merge_sort(array1,0,9))