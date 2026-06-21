import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
import numpy as np
# subplots

#x = np.array([1, 2, 3, 4, 5])
#figure, axes= (plt.subplots(2, 2))

#axes[0, 0].plot(x, x*2, color="red")
#axes[0, 0].set_title("sam")

#axes[0, 1].bar(x, x**2, color="blue")
#axes[0, 1].set_title("ram")

#axes[1, 0].plot(x, x**3, color="green")
#axes[1, 0].set_title("ethan")

#axes[1, 1].hist(x, x**4, color="purple")
#axes[1, 1].set_title("jade")

#plt.tight_layout()

#plt.show()



import pandas as pd



df = pd.read_csv("data.csv")

type_count = (df["Type1"].value_counts())

plt.barh(type_count.index, type_count.values, color="yellow", edgecolor="black")

plt.title("Count of pokemon type")
plt.xlabel("Count")
plt.ylabel("Type")
plt.tight_layout()
plt.show()

