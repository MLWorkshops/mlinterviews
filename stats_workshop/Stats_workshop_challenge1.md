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
```


```python
# SOLUTION (TBD: remove it)

import matplotlib.pyplot as plt
import numpy as np

# coding challenge
# write a function that computes a variance of a given

def compute_variance(values):
    mean = sum(values) / len(values)
    sum_of_squared_deviations_from_mean = 0
    # The variance of a random variable X is the expected value of the squared deviation from the mean [https://en.wikipedia.org/wiki/Variance]
    for value in values:
      sum_of_squared_deviations_from_mean += (value - mean) ** 2
    variance = sum_of_squared_deviations_from_mean / len(values)
    return variance

# zoom poll: answers: 30, 200, 0, -1, I did not solve it today, but I will try later
compute_variance([10, 20, 30, 40, 50])
```


```python

```
