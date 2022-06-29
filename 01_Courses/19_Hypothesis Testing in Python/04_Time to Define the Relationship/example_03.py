"""
# Look ma! Still no parameters!

# Wilcoxon-Mann-Whitney test
# # Also know as the Mann Whitney U test
# # A t-test on the ranks of the numeric input
# # Works on unpaired data
"""
from scipy.stats import rankdata
import pandas as pd
import numpy as np
import pingouin

stack_overflow = pd.read_feather(".\data\stack_overflow.feather")
# print(stack_overflow.head())

# Wilcoxon-Mann-Whitney test setup
age_vs_comp = stack_overflow[['converted_comp','age_first_code_cut']]
age_vs_comp_wide = age_vs_comp.pivot(columns='age_first_code_cut',values='converted_comp')

# Wilcoxon-Mann-Whitney test
alpha=0.01

pingouin.mwu(x=age_vs_comp_wide['child'],
             y=age_vs_comp_wide['adult'],
             alternative='greater')

# Kruskal-Wallis test
# # Kruskal-Wallis test is to Wilcoxon-Mann-Whitney test as ANOVA is to t-test
alpha=0.01

pingouin.kruskal(data=stack_overflow,
                 dv='converted_comp',
                 between='job_sat')