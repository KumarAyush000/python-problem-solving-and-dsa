def is_palindrome(text: str) -> bool:
    """
    Check whether a given string is a palindrome.
    """
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]


if __name__ == "__main__":
    sample = "madam"
    print(is_palindrome(sample))