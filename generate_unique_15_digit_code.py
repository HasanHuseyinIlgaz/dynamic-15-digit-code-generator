import random

weights = {
    7: [2, 3, 1, 4, 5, 2],
    8: [3, 1, 2, 4, 5, 2, 1],
    9: [1, 3, 2, 5, 4, 6, 2, 3],
    10: [2, 3, 1, 4, 6, 5, 2, 3, 4],
    11: [1, 2, 3, 4, 5, 6, 2, 1, 3, 4],
    12: [2, 4, 1, 3, 5, 2, 6, 3, 2, 1, 4],
    13: [3, 1, 2, 5, 4, 2, 6, 3, 4, 1, 2, 3],
    14: [2, 4, 1, 3, 5, 6, 2, 1, 4, 5, 3, 2, 1],
    15: [3, 2, 4, 1, 5, 6, 3, 2, 1, 4, 3, 5, 6, 1],
}


def generate_unique_15_digit_code():
    digits = []

    first_five_digits = [random.randint(0, 9) for _ in range(5)]
    digits.extend(first_five_digits)

    digit_sixth = sum(digits[:5]) % 10
    digits.append(digit_sixth)

    for position in range(7, 16):
        weight_list = weights[position]
        dynamic_mod = digits[-1] + (7 if position == 7 else position + 2)

        if position == 8:
            new_digit = (
                int(sum((w * h) / 2 for w, h in zip(weight_list, digits))) % dynamic_mod
            )
        else:
            new_digit = sum(w * h for w, h in zip(weight_list, digits)) % dynamic_mod

        digits.append(new_digit)

    return "".join(map(str, digits))


finally_digit_code = generate_unique_15_digit_code()
print(f"Generated Code: {finally_digit_code}")
