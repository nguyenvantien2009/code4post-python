'''
Try with T-test in Python. There are 3 types of T-test
- One Sample Test
- Pair Sample Test
- Indenpency Sample Test

Refer to https://www.geeksforgeeks.org/t-test/
And https://www.notion.so/nguyenvantien2009/Different-Z-Test-T-Test-dbd8f17a5f4c4e338228944a94f65753 
'''

from scipy import stats
import numpy as np

# build install random stage.
rng = np.random.default_rng()

# ============================================
# Try with One Same T-test
# ============================================
hypotheris_mean = 0.5
rvs = stats.uniform.rvs(size=50, random_state=rng)
print('Dataset for one sample test', rvs)
one_test = stats.ttest_1samp(rvs, hypotheris_mean)
print('===> Result of one test', one_test)
print('Mean values of dataset is equal 0.5 is right or wrong: ', one_test.pvalue >= 0.05)
print('-------------------------------------------------------')

# ============================================
# Try with Pair sample
# ============================================
rvs_1 = stats.uniform.rvs(size=50, random_state=rng)
rvs_2 = stats.norm.rvs(size=50, random_state=rng)
pair_test =  stats.ttest_rel(rvs_1, rvs_2)
print('===> Result of pair test', pair_test)
print('The 2 datasets are similar?', pair_test.pvalue >= 0.05)
print('-------------------------------------------------------')

# ============================================
# Try with independency sample
# ============================================
rvs_1 = stats.uniform.rvs(size=50, random_state=rng)
rvs_2 = stats.norm.rvs(size=10, random_state=rng)
ind_test = stats.ttest_ind(rvs_1, rvs_2)
print('===> Resul of independency', ind_test)
print('The 2 datasets are simalar?', ind_test.pvalue >= 0.05)
print('-------------------------------------------------------')