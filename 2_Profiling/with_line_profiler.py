"""
pip install line-profiler
"""


# Put @profile under function you want to check.
# This function should be executable.

@profile  # do not pay attention to this error
# ----------------------------------------------------------
def fn_expressive(upper=1_000_000):
    total = 0
    for n in range(upper):
        total += n
    return total


@profile
# ----------------------------------------------------------
def fn_terse(upper=1_000_000):
    return sum(range(upper))


@profile
# ----------------------------------------------------------
def main():
    if fn_expressive() == fn_terse():
        print('[+] Success!')
    else:
        print('[!] Error!')


# ----------------------------------------------------------
if __name__ == "__main__":
    main()

# LineProfiler with console

# kernprof -l -v with_line_profiler.py


# D:\Python\High Performance\2_Profiling>kernprof -l -v with_line_profiler.py
# [+] Success!
# Wrote profile results to with_line_profiler.py.lprof
# Timer unit: 1e-06 s
#
# Total time: 0.530583 s
# File: with_line_profiler.py
# Function: fn_expressive at line 1
#
# Line #      Hits         Time  Per Hit   % Time  Line Contents
# ==============================================================
#      1                                           @profile
#      2                                           # ----------------------------------------------------------
#      3                                           def fn_expressive(upper=1_000_000):
#      4         1          0.4      0.4      0.0      total = 0
#      5   1000001     246544.6      0.2     46.5      for n in range(upper):
#      6   1000000     284032.7      0.3     53.5          total += n
#      7         1          5.3      5.3      0.0      return total
#
# Total time: 0.0236661 s
# File: with_line_profiler.py
# Function: fn_terse at line 10
#
# Line #      Hits         Time  Per Hit   % Time  Line Contents
# ==============================================================
#     10                                           @profile
#     11                                           # ----------------------------------------------------------
#     12                                           def fn_terse(upper=1_000_000):
#     13         1      23666.1  23666.1    100.0      return sum(range(upper))
#
# Total time: 0.943695 s
# File: with_line_profiler.py
# Function: main at line 16
#
# Line #      Hits         Time  Per Hit   % Time  Line Contents
# ==============================================================
#     16                                           @profile
#     17                                           # ----------------------------------------------------------
#     18                                           def main():
#     19         1     943588.4 943588.4    100.0      if fn_expressive() == fn_terse():
#     20         1        107.0    107.0      0.0          print('[+] Success!')
#     21                                               else:
#     22                                                   print('[!] Error!')
