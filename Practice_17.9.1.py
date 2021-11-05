numbers = list(map(int, input("Введите последовательность чисел через пробел\n").split()))
n = int(input("Введите любое число\n"))

def sort(array):
    #return x.sort()
    for i in range(1, len(array)):
        x = array[i]
        idx = i
        while idx > 0 and array[idx - 1] > x:
            array[idx] = array[idx - 1]
            idx -= 1
        array[idx] = x

sort(numbers)

def binary_search(array, element, left, right):
    if left > right:
        return print("Введенное Вами число", element, "не соответствует заданному условию!")

    middle = (right + left) // 2
    if array[middle] >= element and array[middle-1] < element:
        return print(middle - 1, "- это номер позиции элемента списка, который меньше введенного Вами числа", element)
    elif array[middle] > element:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)
print(numbers)
binary_search(numbers, n, 0, len(numbers)-1)