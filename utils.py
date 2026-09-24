def is_valid_name(name):
    if not name:
        return False
    return all(character.isalpha() or character.isspace() for character in name)


def is_valid_phone(phone):
    return phone.isdigit() and len(phone) == 10


def is_valid_pin(pin):
    return pin.isdigit() and len(pin) == 4


def is_valid_amount(amount):
    try:
        value = float(amount)
        return value > 0
    except (TypeError, ValueError):
        return False
