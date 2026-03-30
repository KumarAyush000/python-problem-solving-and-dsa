def find_max(nums: list[int]) -> int:
    if not nums:
        raise ValueError("List cannot be empty")
    return max(nums)


def rotate_array(nums: list[int], k: int) -> list[int]:
    k = k % len(nums)
    return nums[-k:] + nums[:-k]


if __name__ == "__main__":
    print(find_max([4, 1, 9, 2]))
    print(rotate_array([1, 2, 3, 4, 5], 2))