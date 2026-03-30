def two_sum(nums: list[int], target: int) -> list[int]:
    seen = {}

    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i

    return []


if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))