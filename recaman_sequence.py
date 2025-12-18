import matplotlib.pyplot as plt
import numpy as np

#Generating the sequence
num = 0
step = 1
seq=[0]

for i in range(1,100):
    if step == i:
        x = num - step
        if x > 0 and x not in seq:
            seq.append(x)
            num = x
            step+=1
        else:
            num += step
            seq.append(num)
            step += 1
print(seq)
print(len(seq))

#Graph Plot
x = np.arange(0,100,1)
y = seq

plt.plot(x,y)
plt.xlabel("Step Count")
plt.ylabel("Sequence Value")
plt.title("Recaman Sequence Plot")
plt.show()
