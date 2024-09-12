import numpy as np
import matplotlib.pyplot as plt

x_train = np.array([1.0, 2.0])
y_train = np.array([300.0, 500.0])
print (f"x_train.shape = {x_train.shape}")
print (f"y_train.shape = {y_train.shape}")

m = len(x_train) 
print (f"Number of training example is: {m}")

i = 0
x_i = x_train[i]
y_i = y_train[i]

print (f"x^({i}), y^({i}) = ({x_i}, {y_i})")

plt.scatter (x_train, y_train, marker = 'x', c ='r')
plt.title ("Housing Price")
plt.ylabel ("Price (in 1000s of dollars)")
plt.xlabel ("Size (1000s sqft)")
plt.show()