import math


def search_1(my_list, search_value):
    first = 0
    last = len(my_list) - 1
    found = False
    time=0
    while first <= last and not found:
        time+=1
        mid = (first + last) // 2
        if my_list[mid] == search_value:
            found = True
        else:
            if search_value < my_list[mid]:
                last = mid - 1
            else:
                first = mid + 1
    print(time)
    return found


def search_2(my_list, search_value):
    length = len(my_list)
    sqrt_length = int(math.sqrt(length))
    left, right = 0, 0
    found = False
    time=0
    while left < length and my_list[left] <= search_value:
        time+=1
        right = min(length - 1, left + sqrt_length)
        if my_list[left] <= search_value <= my_list[right]:
            break
        left += sqrt_length
    if left >= length or my_list[left] > search_value:
        print(time)
        return found
    right = min(length - 1, right)
    i = left
    while i <= right and my_list[i] <= search_value:
        time+=1
        if my_list[i] == search_value:
            print(time)
            found = True
            return found
        i += 1
    print(time)
    return found
