import dis


# ----------------------------------------------------------
def fn_expressive(upper=1_000_000):
    total = 0
    for n in range(upper):
        total += n
    return total


# ----------------------------------------------------------
def fn_terse(upper=1_000_000):
    return sum(range(upper))


# ----------------------------------------------------------
def main():
    if fn_expressive() == fn_terse():
        print('[+] Success!')
    else:
        print('[!] Error!')


# ----------------------------------------------------------
if __name__ == "__main__":
    dis.dis(main)
    # dis.dis(fn_terse)
    # dis.dis(fn_expressive)

#  18           0 LOAD_GLOBAL              0 (fn_expressive)
#               2 CALL_FUNCTION            0
#               4 LOAD_GLOBAL              1 (fn_terse)
#               6 CALL_FUNCTION            0
#               8 COMPARE_OP               2 (==)
#              10 POP_JUMP_IF_FALSE       22
#
#  19          12 LOAD_GLOBAL              2 (print)
#              14 LOAD_CONST               1 ('[+] Success!')
#              16 CALL_FUNCTION            1
#              18 POP_TOP
#              20 JUMP_FORWARD             8 (to 30)
#
#  21     >>   22 LOAD_GLOBAL              2 (print)
#              24 LOAD_CONST               2 ('[!] Error!')
#              26 CALL_FUNCTION            1
#              28 POP_TOP
#         >>   30 LOAD_CONST               0 (None)
#              32 RETURN_VALUE
