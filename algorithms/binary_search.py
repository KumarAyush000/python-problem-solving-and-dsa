def binary_search(nums: list[int], target: int) -> int:
    """
    Return the index of target in a sorted list.
    Return -1 if not found.
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


if __name__ == "__main__":
    numbers = [1, 3, 5, 7, 9]
    print(binary_search(numbers, 7))