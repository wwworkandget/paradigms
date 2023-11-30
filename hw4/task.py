from functools import reduce
import math


def Pearson_correlation(array_1, array_2):
    if len(array_1) != len(array_2) or len(array_1) == 0 or len(array_2) == 0:
        return None

    srednee_x = sum(array_1) / len(array_1)
    srednee_y = sum(array_2) / len(array_2)

    # Числитель
    r_numerator = reduce(
        lambda x, y: x + y,
        map(lambda x: (x[0] - srednee_x) * (x[1] - srednee_y),
            zip(array_1, array_2)))

    sum_x = reduce(lambda x, y: x + y,
                   map(lambda x: (x - srednee_x)**2, array_1))
    sum_y = reduce(lambda x, y: x + y,
                   map(lambda y: (y - srednee_y)**2, array_2))

    # Знаменатель
    r_denominator = math.sqrt(sum_x * sum_y)
    if r_denominator == 0:
        return None
    return r_numerator / r_denominator


print(Pearson_correlation([1, 2, 3], [4, 8, 6]))
