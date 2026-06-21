import numpy as np
array = np.array([[1,2,3,4,5],
                  [6,7,8,9,10]])

print(np.mean(array))
print(np.std(array))
print(np.var(array))
print(np.argmin(array))

# to sum all columns axis =0
print(np.sum(array,axis=0))

# axis =1 row 
print(np.sum(array,axis=1))