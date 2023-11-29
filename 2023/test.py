import os

for i in range(1, 26):
    folder = "day" + ("0" + str(i) if i < 10 else str(i))

    os.mkdir(folder)

    with open(os.path.join(folder, 'main.py'), 'w') as f:
        f.write("")

    with open(os.path.join(folder, 'input.txt'), 'w') as f:
        f.write("")