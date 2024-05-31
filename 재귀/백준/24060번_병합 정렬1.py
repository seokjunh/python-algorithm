N, K = map(int,input().split())

A = list(map(int, input().split()))

def merge_sort(A):
    if len(A) <= 1:
        return A
    mid = (len(A)+1) // 2
    left = merge_sort(A[:mid])
    right = merge_sort(A[mid:])

    i = j = 0
    sorted_list = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            answer.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            answer.append(right[j])
            j += 1
    while i < len(left):
        sorted_list.append(left[i])
        answer.append(left[i])
        i += 1
    while j < len(right):
        sorted_list.append(right[j])
        answer.append(right[j])
        j += 1
    return sorted_list

answer = []
merge_sort(A)

if len(answer) >= K:
    print(answer[K-1])
else:
    print(-1)