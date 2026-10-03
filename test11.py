import matplotlib.pyplot as plt

label = ['orange', 'apple', 'kiwi']
size = [10, 3, 1]

fig, ax = plt.subplots()
explode = (0, 0, 0.2)
ax.pie(size, labels=label, autopct='%1.2f%%', startangle=90, counterclock=False, colors=['orange', 'red', 'green'], explode=explode)
ax.legend()

plt.show()