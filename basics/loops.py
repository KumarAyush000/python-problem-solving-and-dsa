def print_even_numbers(limit: int) -> list[int]:
    return [num for num in range(1, limit + 1) if num % 2 == 0]


def multiplication_table(number: int) -> list[str]:
    return [f"{number} x {i} = {number * i}" for i in range(1, 11)]


if __name__ == "__main__":
    print("Even numbers:", print_even_numbers(20))
    print("\n".join(multiplication_table(5)))