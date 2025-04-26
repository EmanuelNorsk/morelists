
import math

def fast_sqrt(x):
    # Fast sqrt approximation with a couple of Newton steps
    if x == 0:
        return 0.0
    guess = x * 0.25
    for _ in range(2):  # Newton-Raphson
        guess = 0.5 * (guess + x / guess)
    return guess


def is_angle_at_least_135(dx1, dy1, dx2, dy2):
    dot = dx1 * dx2 + dy1 * dy2
    if dot >= 0:
        return False  # Less than 90°

    len_sq1 = dx1 * dx1 + dy1 * dy1
    len_sq2 = dx2 * dx2 + dy2 * dy2
    if len_sq1 == 0 or len_sq2 == 0:
        return False

    product = fast_sqrt(len_sq1 * len_sq2)

    # cos(135°) ≈ -0.7071
    return dot <= -0.7071 * product


print(is_angle_at_least_135(4, 1, -16, 1))