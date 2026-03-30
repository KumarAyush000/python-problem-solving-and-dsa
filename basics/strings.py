def reverse_string(text: str) -> str:
    return text[::-1]


def count_vowels(text: str) -> int:
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)


def is_palindrome(text: str) -> bool:
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]


if __name__ == "__main__":
    sample = "madam"
    print("Reversed:", reverse_string(sample))
    print("Vowel count:", count_vowels(sample))
    print("Palindrome:", is_palindrome(sample))