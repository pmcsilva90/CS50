def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    digit = 0
    s = s.strip()

    if len(s) < 2 or len(s) > 6:
        return False
    for c in s:
        if c.isdigit():
            digit += 1
            # The first number used cannot be a ‘0’.”
            if digit == 1 and c == '0':
                return False
        # “No periods, spaces, or punctuation marks are allowed.”
        elif not c.isalnum():
            return False
        # “Numbers cannot be used in the middle of a plate"
        elif digit > 0 and c.isalpha():
            return False

    # “All vanity plates must start with at least two letters.”
    # “Numbers must come at the end."
    if not s[0].isalpha() or not s[1].isalpha() or s[-1].isalpha():
        if s[-1].isalpha() and digit == 0:
            return True
        else:
            return False

    return True

main()
