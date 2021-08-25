import asyncio


# ---------------------------------------------------
async def fetch_data():
    print('Start')
    await asyncio.sleep(2)  # I/O pause
    print('Finish')
    return {'data': 1}


# ---------------------------------------------------
async def print_numbers():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.25)


# ---------------------------------------------------
async def main():
    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(print_numbers())

    value = await task1
    print(value)
    await task2


# ---------------------------------------------------
if __name__ == '__main__':
    asyncio.run(main())

# Start
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# Finish
# {'data': 1}
# 8
# 9
