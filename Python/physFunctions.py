def position(v, a, t):
    ix = 0
    result = ix + (v * t) + (0.5 * a * (t ^ 2))
    return result


def velocity(iv, a, t):
    result = iv + (a * t)
    return result


def acceleration(fv, iv, t):
    result = (fv - iv) / t
    return result


def force(m, a):
    result = m * a
    return result


def voltage(i, r):
    result = i * r
    return result


def total_r_in_series(resistors):
    length = len(resistors)
    result = 0
    for i in range(length):
        result = result + resistors[i]
    return result




