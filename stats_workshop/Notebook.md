```python
import matplotlib.pyplot as plt
import numpy as np
from numpy.random import randint

np.random.seed(123456)

number_of_bins = 50
number_of_points = 1000000
#
#
values = np.random.rand(number_of_points)

# Create data
x = range(len(values))
y = values

# Plot
plt.scatter(x, y)
plt.title('Points')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

```


```python
print("Population variance={}".format(np.var(values)))
```


```python
# uniform distribution
plt.hist(values, bins=number_of_bins)
plt.show()
```


```python
def build_sample_distribution(number_of_samples, sample_size, population_data):
    # central limit theorem
    sample_means = []
    for i in range(number_of_samples):
        sample_sum = 0
        for j in range(sample_size):
            # update the s variable with a random
            sample_sum += population_data[randint(len(population_data))]
        sample_mean = float(sample_sum / sample_size)
        sample_means.append(sample_mean)

    plt.hist(sample_means, bins=50, range=(0, 1))
    plt.show()
```


```python
build_sample_distribution(number_of_samples=10000, sample_size=30, population_data=values)
```


```python
import matplotlib.pyplot as plt
import numpy as np

# coding challenge
# write a function that computes a variance of a given list of values

def compute_variance(values):
    mean = sum(values) / len(values)
    sum_of_squared_deviations_from_mean = 0
    # The variance of a random variable X is the expected value of the squared deviation from the mean [https://en.wikipedia.org/wiki/Variance]
    for value in <ADD_VARIABLE_HERE>:
      sum_of_squared_deviations_from_mean += (<ADD EXPRESSION HERE>) ** 2
    variance = <ADD EXPRESSION HERE>
    return variance

print(compute_variance([10, 20, 30, 40, 50]))
```


```python
build_sample_distribution(number_of_samples=10000, sample_size=1, population_data=values)
```


```python
build_sample_distribution(number_of_samples=10000, sample_size=10, population_data=values)
```


```python
build_sample_distribution(number_of_samples=3, sample_size=10, population_data=values)
```


```python
build_sample_distribution(number_of_samples=3, sample_size=3000, population_data=values)
```


```python
import matplotlib.pyplot as plt
import numpy as np
from math import sqrt

# coding challenge
# write a function that computes a z-score for a given number assuming
# that the values follow a normal distribution
# z-score is is the number of standard deviations by which the value of a
# raw score (i.e., an observed value or data point)
# is above or below the mean value of what is being observed or measured. [https://en.wikipedia.org/wiki/Standard_score]

def compute_variance(values):
    mean = sum(values) / len(values)
    sum_of_squared_deviations_from_mean = 0
    # The variance of a random variable X is the expected value of the squared deviation from the mean [https://en.wikipedia.org/wiki/Variance]
    for value in values:
      sum_of_squared_deviations_from_mean += (value - mean) ** 2
    variance = sum_of_squared_deviations_from_mean / len(values)
    return variance

def compute_zscore(values, number):
    mean = <ADD EXPRESSION HERE>
    variance = compute_variance(values)
    standard_deviation = <ADD EXPRESSION HERE>
    z_score = <ADD EXPRESSION HERE>
    return z_score

print(compute_zscore([10, 20, 30, 40, 50], 15))
```
