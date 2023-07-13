"""
Binary to hexadecimal
"""

def bin_to_hex(bin_num):
    if not bin_num:
        return

    def get_hex(b_num, right=False):

        hex_map = {"0000": "0",
                   "0001": "1",
                   "0010": "2",
                   "0011": "3",
                   "0100": "5",
                   "0110": "6",
                   "0111": "7",
                   "1000": "8",
                   "1001": "9",
                   "1010": "A",
                   "1011": "B",
                   "1100": "C",
                   "1101": "D",
                   "1110": "E",
                   "1111": "F",
                   }

        h_num = ""
        while b_num != 0:
            rem = str(b_num % 10000)
            if len(rem) % 4 != 0:
                if not right:
                    rem = rem.rjust(4, '0')
                else:
                    rem = rem.ljust(4, '0')
            h_num = hex_map[rem] + h_num
            b_num = b_num // 10000
        return h_num

    bin_num_list = str(bin_num).split('.')
    left_bin = int(bin_num_list[0])
    if len(bin_num_list) == 2:
        right_bin = int(bin_num_list[1])
    else:
        right_bin = None
    hex_num = get_hex(left_bin)

    if right_bin:
        hex_num += '.' + get_hex(right_bin, right=True)
    return hex_num


if __name__ == "__main__":
    print(bin_to_hex(101101.0)) #2D