


def normalize_number(number):
    return number.upper().replace(" ", "")


def validate_number(number):
    number = normalize_number(number)

    if len(number) != 10:
        return False

    if not number[:2].isalpha():
        return False

    if not number[2:4].isdigit():
        return False

    if not number[4:6].isalpha():
        return False

    if not number[6:].isdigit():
        return False

    return True


def format_number(number):
    number = normalize_number(number)

    return number[:2] + " " + number[2:4] + " " + number[4:6] + " " + number[6:]


print("===== VEHICLE REGISTRATION VALIDATOR =====")

registration = input("Enter vehicle number (Example: TN 09 AB 1234): ")

if validate_number(registration):
    print("Valid Registration Number")
    print("Formatted Number:", format_number(registration))
else:
    print("Invalid Registration Number")

print("\n===== PROGRAM COMPLETED =====")
