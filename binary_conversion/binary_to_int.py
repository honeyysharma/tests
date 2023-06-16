"""
binary to int
1    0    0
2^2 2^1 2^0
= 2^2 x 1 + 2^1 x 0 + 2^0 x 0
= 4 x 1   + 2 X 0   + 1 x 0
= 4       + 0       + 0
= 4
"""


def binary_to_int(bin_num):
    result = 0
    i = 0
    while bin_num != 0:
        result += (2 ** i) * (bin_num % 10)
        bin_num = bin_num // 10
        i += 1
    return result


if __name__ == "__main__":
    result = binary_to_int(10)
    print('Result: {0}'.format(result))
