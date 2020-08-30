import matplotlib.pyplot as plt

set1 = [x for x in range(50)]
set2 = [x * 2 for x in range(100)]
plt.plot(set1)
plt.plot(set2)
plt.ylabel('some numbers')
plt.show()
