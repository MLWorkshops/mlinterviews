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

def compute_zscore(values, number):
    mean = <ADD EXPRESSION HERE>
    variance = compute_variance(values)
    standard_deviation = <ADD EXPRESSION HERE>
    z_score = <ADD EXPRESSION HERE>
    return z_score
```


```python
# SOLUTION (TBD: remove it)

def compute_zscore(values, number):
    mean = sum(values) / len(values)
    variance = compute_variance(values)
    standard_deviation = sqrt(variance)
    z_score = (number - mean) / standard_deviation
    return z_score
```


```python

```
