import matplotlib.style
import matplotlib.pyplot as plt

print(matplotlib.style.available)

matplotlib.style.use('ggplot')
fig, ax = plt.subplots()
ax.plot([0, 10], [0, 20])
ax.set_title('日本語のタイトル')
ax.text(5, 15, '日本語のテキスト', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

plt.show()