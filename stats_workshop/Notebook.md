```python
import matplotlib.pyplot as plt
import numpy as np
from numpy.random import randint

np.random.seed(123456)

number_of_bins = 50
number_of_points = 100000
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
build_sample_distribution(number_of_samples=10000, sample_size=1, population_data=values)
```


```python
build_sample_distribution(number_of_samples=10000, sample_size=2, population_data=values)
```


```python
build_sample_distribution(number_of_samples=10000, sample_size=3, population_data=values)
```


```python
build_sample_distribution(number_of_samples=10000, sample_size=10, population_data=values)
```


```python
build_sample_distribution(number_of_samples=10000, sample_size=30, population_data=values)
```


```python
build_sample_distribution(number_of_samples=100, sample_size=3000, population_data=values)
```


```python
build_sample_distribution(number_of_samples=3, sample_size=3000, population_data=values)
```


```python

```
