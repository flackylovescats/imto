def guess_number(target, nums, method):
    """
    A function that finds the target number in array

    Parameters
    ----------
    target : int
        Target number to find
    nums : [int]
        Array to find target in, might be unsorted, every element is unique, contains target
    method : string
        Either 'slow' - enumeration through every element, or 'binary' - binary search on sorted array

    Returns
    -------
    num : int
        Number that was found
    iterations : int
        Amount of guesses spent to find a target

    In case of unknown method or if target was not found returns (-1, -1)
    """

    if method == 'slow':
        for i in range(len(nums)):
            if nums[i] == target:
                return nums[i], i+1
    elif method == 'binary':
        nums.sort()
        left = -1
        right = len(nums)
        mid = (left + right) // 2
        a = 1
        while nums[mid] != target:
            if nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid
            mid = (left + right) // 2
            a = a + 1
        return nums[mid], a
    return -1, -1

def read_input():
    """
    A function that reads user input and writes back a result

    Parameters
    ----------
    none

    Returns
    -------
    none

    """
    target = int(input('искомое число: '))
    start = int(input('начало диапазона: '))
    end = int(input('конец диапазона: '))
    nums = list(range(start, end+1))
    method = input('алгоритм (slow/binary): ')
    num, count = guess_number(target, nums, method)
    print('число', num, 'найдено за', count, 'попыток')

if __name__ == "__main__":
    read_input()