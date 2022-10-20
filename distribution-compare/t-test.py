# import libaries need.
from scipy import stats
import numpy as np

# build install random stage.
rng = np.random.default_rng()

# generate random data.
rvs1 = stats.norm.rvs(loc=5, scale=10, size=500, random_state=rng)
rvs2 = stats.norm.rvs(loc=5, scale=10, size=500, random_state=rng)
rs = stats.ttest_ind(rvs1, rvs2)

# print result.
print(rs)