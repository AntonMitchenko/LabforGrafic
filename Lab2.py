import matplotlib.pyplot as plt

first = []
second = []
main_text =[]

file = open("DS4.txt")
with file as a:
    for line in a:
        main_text.append([int(x) for x in line.split()])
for i in range(len(main_text)):
    for j in range(1):
        first.append(main_text[i][0])
        second.append(960 - main_text[i][1])
plt.figure('Малюнок за датасетом')
plt.scatter(first, second)

plt.show()
plt.close()
file.close()
