import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
import numpy as np

#x1 = [0, 1, 2, 1, 2, 0, 1, 5, 7, 4, 9]
#y1 = [55, 90, 65, 50, 80, 34, 56, 67, 56, 34, 90]

#x2 = [0, 1, 1, 2, 4, 3, 1, 2, 7, 3, 3]
#y2 = [55, 90, 74, 67, 20, 34, 60, 34, 56, 34, 69]


#plt.scatter(x1, y1, color="skyblue", alpha=0.5, s=180, label= "Class A")

#plt.scatter(x2, y2, color="red", alpha=0.5, s=180, label="Class B")


plt.title("Exam scores")
plt.xlabel("Score")
plt.ylabel("No of Student")
#plt.legend()

scores = np.random.normal(loc=80, scale=10, size=100)
scores = np.clip(scores, 0, 100)
plt.hist(scores, bins=10, color="yellow", edgecolor="black")



plt.show()