def check_number(num: int) -> str:
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    return "Zero"


def is_eligible_to_vote(age: int) -> bool:
    return age >= 18


if __name__ == "__main__":
    print(check_number(-5))
    print("Eligible to vote:", is_eligible_to_vote(21))