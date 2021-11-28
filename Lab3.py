import matplotlib.pyplot as plt
import math
first = []
second = []
main_text =[]
x=[]
y=[]
print(math.radians(40))

my_file = open("DS4.txt")
with my_file as f:
    for line in f:
            main_text.append([int(x) for x in line.split()])
for i in range(len(main_text)):
    for j in range(1):
        first.append(main_text[i][0])
        second.append(960 - main_text[i][1])
        first[i] -= 480
        second[i] -= 480
        x.append(int(first[i]) * math.cos(math.radians(50)) - int(second[i]) * math.sin(math.radians(50)))
        y.append(int(first[i]) * math.sin(math.radians(50)) + int(second[i]) * math.cos(math.radians(50)))
        x[i] += 480
        y[i] += 480
        first[i] += 480
        second[i] += 480
plt.figure('Афінне перетворення малюнка за датасетом')
plt.scatter(first, second)
plt.scatter(x, y)
plt.show()
plt.close()
my_file.close()