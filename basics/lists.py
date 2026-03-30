def find_max(nums: list[int]) -> int:
    if not nums:
        raise ValueError("List cannot be empty")
    return max(nums)


def remove_duplicates(nums: list[int]) -> list[int]:
    return list(dict.fromkeys(nums))


def sum_list(nums: list[int]) -> int:
    return sum(nums)


if __name__ == "__main__":
    numbers = [1, 2, 2, 3, 4, 4, 5]
    print("Max:", find_max(numbers))
    print("Without duplicates:", remove_duplicates(numbers))
    print("Sum:", sum_list(numbers))