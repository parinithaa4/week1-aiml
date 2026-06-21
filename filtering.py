import numpy as np

#ages = np.array([[21,17,19,20,16,30,18,65],
                 #[39,22,15,99,18,19,20,21]])

#teenagers = ages[ages < 18]
#adults = ages[(ages > 18) | ( ages < 65 )]
#print (teenagers)
#print(adults)

# randon numbers 

rng = np.random.default_rng()
#print(rng.integers(low = 123,high = 879 , size= (3,2)))

#array = np.array([1,2,3,4,5])
#rng.shuffle(array)
#print(array)
#print(np.random.uniform(low=-1, high=1 ,size=(3,2)))

fruits = np.array(["apple","orange","pineapple"])
fruit = rng.choice(fruits)
print(fruit)





