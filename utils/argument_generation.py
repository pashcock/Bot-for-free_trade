import random
import string


async def generation():
    return ''.join(random.choice(string.ascii_letters)+str(random.randint(0, 9)) for i in range(5))
