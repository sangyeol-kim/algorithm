
#     int i = 0
#     int n = 0
#     int * a = NULL
#     int left_max = -1
#     int last_max = -1
#     int right_subarray_count = 0
#     printf("Enter number of elements: ")
#     scanf("%d", & n)
#     a = (int * )malloc(sizeof(int)*n)
#     for (
#         i < n
#         i++) {
#         printf("Enter element [%d]: ", i)
#         scanf("%d", & a[i])
#     }


def solution(T):
    # 배열은 T
    right_count = 0

    left_max = T[0]
    last_max = T[0]

    if(min(T) < -10000000000 and max(T) > 10000000000):
        return -1
    elif(len(T) >= 2 and len(T) <= 300000):
        return -1

    for i in range(1, len(T)):
        if (left_max < T[i]):
            right_count += 1
            last_max = T[i]
        else:
            right_count = 0
            left_max = last_max
    return len(T) - right_count


T = [5, -2, 3, 8, 6]
print(solution(T))

#     left_max = a[0]
#     last_max = a[0]
#     for (i=1
#          i < n
#          i++) {
#         if (left_max < a[i]) {
#             right_subarray_count++
#             last_max = a[i]
#         }
#         else {
#             right_subarray_count = 0
#             left_max = last_max
#         }
#     }
#     printf("Number of elements in right sub-array(or winter days) is: %d\n",
#            n - right_subarray_count)
#     return 0
# }
