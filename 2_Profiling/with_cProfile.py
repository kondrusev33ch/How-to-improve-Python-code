import cProfile


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
        for _ in range(99):
            fn_terse()
        print('[+] Success!')
    else:
        print('[!] Error!')


# ----------------------------------------------------------
if __name__ == "__main__":
    # cProfile.run('main()') - without saving report
    cProfile.run('main()', 'output.dat')

    import pstats

    with open('out_time.txt', 'w') as f:
        p = pstats.Stats('output.dat', stream=f)
        p.sort_stats('time').print_stats()

    with open('out_calls.txt', 'w') as f:
        p = pstats.Stats('output.dat', stream=f)
        p.sort_stats('calls').print_stats()

# cProfile with console

# python -m cProfile -s cumulative with_cProfile.py      - show stats
# python -m cProfile -o profile.stats with_cProfile.py   - save stats to profile.stats

# After saving stats, you can sort them:
# Open python console
# >>> import pstats
# >>> p = pstats.Stats('profile.stats')
# >>> p.sort_stats('cumulative')
# >>> p.print_stats()

# TO VISUALIZE INFORMATION USE SnakeViz!
# https://jiffyclub.github.io/snakeviz/
