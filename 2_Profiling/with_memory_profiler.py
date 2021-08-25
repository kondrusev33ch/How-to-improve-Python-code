"""
pip install memory_profiler
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

# MemoryProfiler with console

# python -m memory_profiler with_memory_profiler.py


# D:\Python\High Performance\2_Profiling>python -m memory_profiler with_memory_profiler.py
# [+] Success!
# Filename: with_memory_profiler.py
#
# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#      9   40.250 MiB   40.250 MiB           1   @profile  # do not pay attention to this error
#     10                                         # ----------------------------------------------------------
#     11                                         def fn_expressive(upper=1_000_000):
#     12   40.250 MiB    0.000 MiB           1       total = 0
#     13   40.273 MiB    0.016 MiB     1000001       for n in range(upper):
#     14   40.273 MiB    0.008 MiB     1000000           total += n
#     15   40.273 MiB    0.000 MiB           1       return total
#
#
# Filename: with_memory_profiler.py
#
# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#     18   40.273 MiB   40.273 MiB           1   @profile
#     19                                         # ----------------------------------------------------------
#     20                                         def fn_terse(upper=1_000_000):
#     21   40.277 MiB    0.004 MiB           1       return sum(range(upper))
#
#
# Filename: with_memory_profiler.py
#
# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#     24   40.238 MiB   40.238 MiB           1   @profile
#     25                                         # ----------------------------------------------------------
#     26                                         def main():
#     27   40.277 MiB   40.277 MiB           1       if fn_expressive() == fn_terse():
#     28   40.277 MiB    0.000 MiB           1           print('[+] Success!')
#     29                                             else:
#     30                                                 print('[!] Error!')
