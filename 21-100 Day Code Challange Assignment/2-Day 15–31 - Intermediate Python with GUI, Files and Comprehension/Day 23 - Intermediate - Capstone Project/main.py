import random
# print(random.randint(-300, 320))

color = []

def random_color(color):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    r_color = (r, g, b)
    for new_color in r_color:
        color.append(new_color)

random_color(color)
print(tuple(color))