import math
import time
import random

NUMBER_OF_ELEMENTS_IN_TEST_LIST = 10000
NUMBER_OF_TESTS = 10
RAND_MAX = 100000

def generate_list(number_of_elements):
    list_ = [0] * number_of_elements
    for index in range(number_of_elements):
        list_[index] = random.randint(-RAND_MAX, RAND_MAX)
    return list_


def BubbleSort(list_):
    swapped = True
    last_index = len(list_)
    while swapped:
        swapped = False
        for index in range(last_index - 1):
            if list_[index] > list_[index + 1]:
                list_[index], list_[index + 1] = list_[index + 1], list_[index]
                swapped = True
        last_index -= 1
    return list_

def selection_sort(list_):
    for i in range(0, len(list_) - 1):
        minimum = i
        for j in range(i + 1, len(list_)):
            if list_[j] < list_[minimum]:
                minimum = j
        list_[i], list_[minimum] = list_[minimum], list_[i]
    return list_

def insertion_sort(list_):
    for i in range(1, len(list_)):
        k = list_[i]
        j = i - 1
        while (j >= 0 and k < list_[j]):
            list_[j + 1] = list_[j]
            j = j - 1
        list_[j + 1] = k
    return list_

def binary_sort(list_):
    for i in range(len(list_)):
        key = list_[i]
        start, end = 0, i - 1
        while start < end:
            mid = start + (end - start) // 2
            if key < list_[mid]:
                end = mid
            else:
                start = mid + 1
        for j in range(i, start + 1,-1):
            list_[j] = list_[j - 1]
        list_[start] = key
    return list_

def merge(list1, list2):
    index1 = 0
    index2 = 0
    list3 = []
    while (index1 < len(list1)) and (index2 < len(list2)):
        if list1[index1] < list2[index2]:
            list3.append(list1[index1])
            index1 += 1
        else:
            list3.append(list2[index2])
            index2 += 1
    while (index1 < len(list1)):
        list3.append(list1[index1])
        index1 += 1
    while (index2 < len(list2)):
        list3.append(list2[index2])
        index2 += 1
    return list3

def merge_sort(list_):
    if len(list_) > 2:
        middle = len(list_) // 2
        list_[: middle] = merge_sort(list_[: middle])
        list_[middle :] = merge_sort(list_[middle :])
        list_ = merge(list_[: middle], list_[middle :])
    elif len(list_) == 0:
        return None
    elif len(list_) == 1:
        return list_
    elif len(list_) == 2:
        if list_[0] > list_[1]:
            list_ = list_[::-1]
    return list_

def quick_sort(list_):
    if len(list_) <= 1:
        return(list_)
    else:
        elem = list_[0]
        left = [i for i in list_ if i < elem]
        center = [i for i in list_ if i == elem]
        right = [i for i in list_ if i > elem]
        return(quick_sort(left) + center + quick_sort(right))

def quick_sort1(list_):
    if len(list_) <= 1:
        return list_
    elif len(list_) == 2:
        if list_[0] > list_[1]:
            list_ = list_[::-1]
        return list_
    else:
        left = []
        right = []
        center = []
        elem = list_[0]
        for i in list_:
            if i < elem:
                left.append(i)
            elif i == elem:
                center.append(i)
            elif i > elem:
                right.append(i)
        return quick_sort(left) + center + quick_sort(right)

def sort_check(list_):
    for index in range(len(list_) - 1):
        if list_[index] > list_[index + 1]:
            return False
    return True

def test(func):
    total_timer = 0
    for test_number in range(NUMBER_OF_TESTS):
        test_list = generate_list(NUMBER_OF_ELEMENTS_IN_TEST_LIST)
        timer = time.time()
        test_list = func(test_list)
        timer = time.time() - timer
        total_timer += timer
        if sort_check(test_list):
            print("Required time in test №", test_number + 1, "is", timer, "seconds")
        else:
            print("Error in test №", test_number + 1)
    print("Required time for", NUMBER_OF_TESTS, "tests is", total_timer, "seconds")
    print("Average time for", NUMBER_OF_TESTS, "tests is", total_timer/NUMBER_OF_TESTS, "seconds")

def search_test(func):
    total_timer = 0
    test_list = sorted(generate_list(NUMBER_OF_ELEMENTS_IN_TEST_LIST))
    for test_number in range(NUMBER_OF_TESTS):
        timer = time.time()
        search_elem = random.randint(-RAND_MAX, RAND_MAX)
        answer = func(test_list, search_elem)
        timer = time.time() - timer
        total_timer += timer
        if not(search_check(test_list, search_elem, answer)):
            print("Error in test №", test_number + 1)
    print("Total time for", NUMBER_OF_TESTS, "tests is", total_timer, "seconds")
    print("Average time for", NUMBER_OF_TESTS, "tests is", total_timer/NUMBER_OF_TESTS, "seconds")

def simple_search(list_, search_elem):
    for index in range(len(list_)):
        if list_[index] == search_elem:
            return index
    return None

def binary_search(list_, search_elem):
    search_left = 0
    search_right = len(list_) - 1
    while search_left < search_right:
        search_middle = (search_left + search_right) // 2
        if search_elem > list_[search_middle]:
            search_left = search_middle + 1
        elif search_elem < list_[search_middle]:
            search_right = search_middle - 1
        else:
            return search_middle
    if search_left == search_right:
        if list_[search_left] == search_elem:
            return search_left
        else:
            return None
    return None


def search_check(list_, search_elem, answer):
    if answer == None:
        for index in range(len(list_)):
            if list_[index] == search_elem:
                return False
        return True
    else:
        '''
        for index in range(answer):
            if list_[index] == search_elem:
                return False
        '''
        if list_[answer] == search_elem:
            return True
        else:
            return False


search_test(simple_search)
search_test(binary_search)
test(BubbleSort)
test(selection_sort)
test(insertion_sort)
test(merge_sort)
test(quick_sort)
test(quick_sort1)
test(binary_sort)
