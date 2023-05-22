def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def print_gcd(a, d):
    q = a // d
    r = a % d

    if r == 0:
        print(f"{a} = {q} * {d} + {r}")
        print(f"Great common divisor is {d}")
        print("-------------------")
        return d
    else:
        print(f"{a} = {q} * {d} + {r}")
        return print_gcd(d, r)


def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0

    gcd, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y


def print_bezout(a, b):
    gcd, x, y = extended_gcd(a, b)
    print("BEZOUT'S IDENTITY")
    print(f"s = {x}, t = {y}")
    print(" ")
    print(f"{a} * {x} + {b} * {y} = {gcd}")
    print("-------------------")


def print_diofantic(a, b, c):
    D, s, t = extended_gcd(a, b)
    if c % D != 0:
        print("No solution")
        return

    a_m = a // D
    b_m = b // D
    c_m = c // D

    print("DIOFANTIC EQUATION")
    print(f"a' = {a_m}, b' = {b_m}, c' = {c_m}")
    print(" ")

    dio = [s * c_m , t * c_m]

    print(f"(x,y) = ({dio[0]} - {b_m}*k, {dio[1]} + {a_m}*k)")
    print("-------------------")


def print_all(a, b, *c):
    print("GREAT COMMON DIVISOR")
    print("-------------------")
    print_gcd(a, b)
    print_bezout(a, b)
    if c:
        print_diofantic(a, b, c[0])


if __name__ == "__main__":
    while True:
        print("Enter a, b, c (optional) to calculate:")
        a = input("Enter a: ")
        b = input("Enter b: ")
        c = input("Enter c: ")
        print(" ")
        print(" ")
        if c:
            print_all(int(a), int(b), int(c))
        else:
            print_all(int(a), int(b))

        print(" ")
