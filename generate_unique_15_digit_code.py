import random


def generate_unique_15_digit_code():
    first_five_digits = [random.randint(0, 9) for _ in range(5)]
    digit_sixth = sum(first_five_digits) % 10
    first_six_digits = first_five_digits + [digit_sixth]

    weights_for_seventh = [2, 3, 1, 4, 5, 2]
    dynamic_mod_for_seventh = digit_sixth + 7
    digit_seventh = (
        sum(w * h for w, h in zip(weights_for_seventh, first_six_digits))
        % dynamic_mod_for_seventh
    )
    first_seven_digits = first_six_digits + [digit_seventh]

    weights_for_eighth = [3, 1, 2, 4, 5, 2, 1]
    dynamic_mod_for_eighth = digit_seventh + 5
    digit_eighth = (
        int(sum((w * h) / 2 for w, h in zip(weights_for_eighth, first_seven_digits)))
        % dynamic_mod_for_eighth
    )
    first_eight_digits = first_seven_digits + [digit_eighth]

    weights_for_ninth = [1, 3, 2, 5, 4, 6, 2, 3]
    dynamic_mod_for_ninth = digit_eighth + 11
    digit_ninth = (
        sum(w * h for w, h in zip(weights_for_ninth, first_eight_digits))
        % dynamic_mod_for_ninth
    )
    first_nine_digits = first_eight_digits + [digit_ninth]

    weights_for_tenth = [2, 3, 1, 4, 6, 5, 2, 3, 4]
    dynamic_mod_for_tenth = digit_ninth + 13
    digit_tenth = (
        sum(w * h for w, h in zip(weights_for_tenth, first_nine_digits))
        % dynamic_mod_for_tenth
    )
    first_ten_digits = first_nine_digits + [digit_tenth]

    weights_for_eleventh = [1, 2, 3, 4, 5, 6, 2, 1, 3, 4]
    dynamic_mod_for_eleventh = digit_tenth + 17
    digit_eleventh = (
        sum(w * h for w, h in zip(weights_for_eleventh, first_ten_digits))
        % dynamic_mod_for_eleventh
    )
    first_eleven_digits = first_ten_digits + [digit_eleventh]

    weights_for_twelfth = [2, 4, 1, 3, 5, 2, 6, 3, 2, 1, 4]
    dynamic_mod_for_twelfth = digit_eleventh + 19
    digit_twelfth = (
        sum(w * h for w, h in zip(weights_for_twelfth, first_eleven_digits))
        % dynamic_mod_for_twelfth
    )
    first_twelve_digits = first_eleven_digits + [digit_twelfth]

    weights_for_thirteenth = [3, 1, 2, 5, 4, 2, 6, 3, 4, 1, 2, 3]
    dynamic_mod_for_thirteenth = digit_twelfth + 23
    digit_thirteenth = (
        sum(w * h for w, h in zip(weights_for_thirteenth, first_twelve_digits))
        % dynamic_mod_for_thirteenth
    )
    first_thirteen_digits = first_twelve_digits + [digit_thirteenth]

    weights_for_fourteenth = [2, 4, 1, 3, 5, 6, 2, 1, 4, 5, 3, 2, 1]
    dynamic_mod_for_fourteenth = digit_thirteenth + 29
    digit_fourteenth = (
        sum(w * h for w, h in zip(weights_for_fourteenth, first_thirteen_digits))
        % dynamic_mod_for_fourteenth
    )
    first_fourteen_digits = first_thirteen_digits + [digit_fourteenth]

    weights_for_fifteenth = [3, 2, 4, 1, 5, 6, 3, 2, 1, 4, 3, 5, 6, 1]
    dynamic_mod_for_fifteenth = digit_fourteenth + 31
    digit_fifteenth = (
        sum(w * h for w, h in zip(weights_for_fifteenth, first_fourteen_digits))
        % dynamic_mod_for_fifteenth
    )

    final_code = first_fourteen_digits + [digit_fifteenth]
    return "".join(map(str, final_code))


fifteen_digit_code = generate_unique_15_digit_code()
print(f"Generated Code: {fifteen_digit_code}")
