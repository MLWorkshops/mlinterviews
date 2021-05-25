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
```


```python
# SOLUTION (TBD: remove it)

import matplotlib.pyplot as plt
import numpy as np
from math import sqrt

def compute_variance(values):
    mean = sum(values) / len(values)
    sum_of_squared_deviations_from_mean = 0
    # The variance of a random variable X is the expected value of the squared deviation from the mean [https://en.wikipedia.org/wiki/Variance]
    for value in values:
      sum_of_squared_deviations_from_mean += (value - mean) ** 2
    variance = sum_of_squared_deviations_from_mean / len(values)
    return variance

def compute_zscore(values, number):
    mean = sum(values) / len(values)
    variance = compute_variance(values)
    standard_deviation = sqrt(variance)
    z_score = (number - mean) / standard_deviation
    return z_score

# zoom poll: answers: 0, 1.06, 1, -1.06, I did not solve it today, but I will try later
compute_zscore([10, 20, 30, 40, 50], 15)
```


```python

```
