import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from matplotlib.ticker import PercentFormatter
import numpy as np
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

with open('ciphertext.txt', 'r') as f:
    ciphertext = f.read()

# print(ciphertext)

char_count = {}

print(list(ciphertext))

for letter in list(LETTERS):
    char_count[letter] = ciphertext.count(letter)

print(len(char_count))

fig, ax = plt.subplots(figsize = (7, 7))

ax.bar(range(len(char_count)), list(char_count.values()), align='center')
plt.xticks(range(len(char_count)), list(char_count.keys()))
# ticker.PercentFormatter(xmax=100, decimals=None, symbol='%', is_latex=False)
ax.yaxis.set_major_formatter(mtick.PercentFormatter(xmax=len(ciphertext)))

plt.show()