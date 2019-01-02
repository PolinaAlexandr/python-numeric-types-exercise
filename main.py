import math


def square_area(side_size):
    return side_size * side_size


def rectangle_area(first_side, second_side):
    return first_side * second_side


def triangle_area(first_side, second_side, last_side):
    return first_side * second_side * last_side


def parallelogram_area_sin(first_side, second_side, degree):
    if degree >= 180:
        print("Sorry, but your parallelogram could not exist")
    else:
        return first_side * second_side * degree


def parallelogram_area_base(base, height):
    return base * height


def degree_to_radians(degree):
    return math.radians(degree)


def radians_to_degrees(radian):
    return math.degrees(radian)


def square_equation_roots(quadratic_coefficient, linear_coefficient, constant):
    discriminant = linear_coefficient**2 - 4 * (quadratic_coefficient * constant)
    if discriminant < 0:
        print("This equation has no roots")
        return None
    elif discriminant == 0:
        x = -linear_coefficient / (2 * quadratic_coefficient)
        print("Equation {}x^2 + {}x + {} = 0 has one following root\n {}"
              .format(quadratic_coefficient, linear_coefficient, constant, x))
        return x
    else:
        x_1 = (-linear_coefficient + math.sqrt(discriminant)) / (2 * quadratic_coefficient)
        x_2 = (-linear_coefficient - math.sqrt(discriminant)) / (2 * quadratic_coefficient)
        #  TODO: return list instead of tuple
        return x_1, x_2


def is_leap(year):
    if year <= 0:
        print("Sorry this year could not exist")
    else:
        return year % 4 == 0 and (year % 100 != 0) or (year % 400 == 0)
if __name__ == "__main__":
    pass