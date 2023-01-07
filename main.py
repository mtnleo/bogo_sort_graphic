import random

def bogo_sort(numbers):

    for i in range(0, len(numbers)):
        get_pos = random.randint(i, len(numbers) - 1)
        aux = numbers[i]
        numbers[i] = numbers[get_pos]
        numbers[get_pos] = aux

    return numbers

def bogo_check(numbers):
    ordered = True

    for i in range(0, len(numbers)):
        if i != len(numbers) - 1:
            if numbers[i] > numbers[i+1]:
                return False

    return ordered

if __name__ == "__main__":
    my_list = [9, 3, 1, 6]
    bogo_sorted_list =  bogo_sort(my_list)
    print("List bogo sorted -> ", bogo_sorted_list)
    print("Is it sorted properly? ", bogo_check(bogo_sorted_list))