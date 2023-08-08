import asyncio


async def print_numbers():
    for i in range(1, 11):
        await asyncio.sleep(1)
        print(i)


def test(num=5):
    return num


print(test())
print(test(50))
print(test(14))
print(test(12))
asyncio.run(print_numbers())
