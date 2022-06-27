import random

colors_correct = [
    '#000000',
    '#FFFFFF'
]

colors_incorrect = [
    '#GGGGGGGG',
    '#HHHHHHHH',
    '000000000'
]

color_random_generate_correct = []
for _ in range(45):
    color = "#" + ''.join([random.choice('0123456789ABCDEF') for _ in range(6)])
    color_random_generate_correct.append(''.join(color))

colors = colors_correct + colors_incorrect + color_random_generate_correct
