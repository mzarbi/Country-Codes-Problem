import random

for i in range(5):
    codesCount = random.randint(10, 20)
    vals = {}
    for i in range(codesCount):
        code = random.randint(1, 200)
        price = random.randint(100, 500) * 0.01
        vals.update({code: round(price,3)})

    print vals