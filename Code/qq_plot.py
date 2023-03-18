import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

# Generate a sample of 100 observations from a normal distribution
sample = np.random.normal(size=100)

print(sample)

plt.hist(sample)
plt.show()

# Create the Q-Q plot
sm.qqplot(sample, line='s')
plt.show()