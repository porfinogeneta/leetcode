# def numSums(N):
#     def sumDigits(n):
#         sum = 0
#         while n != 0:
#             remainder = n % 10
#             sum += remainder
#             n //= 10
#         return sum
#     # nasza docelowa wartość
#     target = sumDigits(N)
#     r = [(i, i + 9) for i in range(0,500, 10)]
#     print(r)
#     ranges = [(i, 10 + i%100 - 1) for i in range(100)]
#     print(ranges)
#     # index tupli z danym przedziałem
#     index_tuple = 0
#     for i in range(len(ranges)):
#         if target >= ranges[i][0] and target <= ranges[i][1]:
#             index_tuple = i
#             break
#     print(index_tuple, ranges[index_tuple])

def numSums(N):
    def sumDigits(n):
        total = 0
        while n != 0:
            remainder = n % 10
            total += remainder
            n //= 10
        return total

    digit_sum = sumDigits(N)
    target = digit_sum * 2

    # Get the number of digits in the input number N
    num_digits = len(str(N))

    # Calculate the number that is twice the number of digits
    result = int('1' + '0' * (num_digits - 1)) * 2

    print("The number that is twice the number of digits of", N, "is:", result)


def max_sum_digits(A):
    hashmap = []
    max_sum = -1
    def digits(n):
        first_digit = -1
        last_digit = -1
        while n != 0:
            remainder = n % 10
            if first_digit == -1:
                first_digit = remainder
            if n // 10 == 0:
                last_digit = remainder
            n //= 10
        return first_digit,last_digit

    for n in A:
        first_last = digits(n)
        for i in range(len(hashmap)):
            if first_last == hashmap[i]:
                if A[i] + n >= max_sum:
                    max_sum = A[i] + n
        hashmap.append(first_last)

    return max_sum

if __name__ == '__main__':
    print(numSums(499))
    # print(max_sum_digits([30,909,3190,99,3990,9009]))
    data = [68.0,
    67.1,
    66.4,
    65.6,
    64.6,
    61.8,
    61.0,
    60.0]

    T = [0,10,20,30,40,80,90,95]

    res = 0
    for i in range(0,len(T)):
        res += data[i]

    print(res)
