def contains_duplicate(nums: list[int]) -> bool:
    return len(nums) != len(set(nums))


def frequency_count(nums: list[int]) -> dict[int, int]:
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
    return freq


if __name__ == "__main__":
    print(contains_duplicate([1, 2, 3, 1]))
    print(frequency_count([1, 2, 2, 3, 3, 3]))