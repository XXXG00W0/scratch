import math
def findMedianHelper(lst: list):
    mid = len(lst)//2
    if len(lst) % 2 == 0:
        return (lst[mid] + lst[mid-1])/2.0
    else:
        return lst[mid]

def findMedian(lst: list):
    if len(lst) <= 10:
        lst.sort()
        return findMedianHelper(lst)
    sub_lst = [lst[i: i+5] for i in range(0, len(lst)-5, 5)]
    sub_lst = [sorted(i) for i in sub_lst]
    median_lst = [i[2] for i in sub_lst]
    median_star = findMedian(median_lst)
    lst_a = [i[:3] for i in sub_lst if i[2] < median_star]
    lst_b = [i[2:] for i in sub_lst if i[2] > median_star]
    lst = [i for i in lst if i not in lst_a + lst_b]
    findMedian(lst)

print(findMedian([i for i in range(20)]))