
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def readable_gcd(a, d):
    q = a // d
    r = a % d

    if r == 0:
        print(f"{a} = {q} * {d} + {r}")
        print("Great common divisor is", end=" ")
        return d
    else:
        print(f"{a} = {q} * {d} + {r}")
        return readable_gcd(d, r)

def main():
    print(readable_gcd(658, 371))

if __name__ == "__main__":
    main()