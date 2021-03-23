import numpy as np
import matplotlib.pyplot as plt

run_no = '4'
data = np.loadtxt('./gofr_'+run_no, delimiter='         ', usecols = (0,2))

plt.scatter(data[:,0],data[:,1])
plt.show()
