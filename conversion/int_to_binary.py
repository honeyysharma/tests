"""
result = ''
num = 4
result = str(4 % 2) + '' = 0

num = num // 2 = 4 // 2 = 2
result = str(2%2) + '0' = 00

num = num // 2 = 2 // 2 = 1
result = str(1%2) + '00' = 100
"""

def int_to_binary(num):
    result = ""
    while num != 0:
        result = str(num % 2) + result
        num = num // 2
    return int(result)


if __name__ == "__main__":
    result = int_to_binary(4)
    print('Result: {0}'.format(result))
    print('{0:b}'.format(4))

    s = "Hello World"
    print(s.split(2))