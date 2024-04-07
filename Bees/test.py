MOD = 10**9 + 7


def sum_of_divisors(k):
    divisor_sum = 0
    for i in range(1, k):
        if k % i == 0:
            divisor_sum = (divisor_sum + i) % MOD
    return divisor_sum


def is_straightforward(k):
    for i in range(2, int(k**0.5) + 1):
        if k % i == 0:
            return False
    return True


def main():
    k = int(input())
    if is_straightforward(k):
        print(sum_of_divisors(k))
    else:
        print("NOT STRAIGHTFORWARD")


if __name__ == "__main__":
    main()
