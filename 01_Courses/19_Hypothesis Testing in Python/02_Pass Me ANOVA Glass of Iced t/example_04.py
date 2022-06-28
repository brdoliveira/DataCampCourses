"""
# P-hacked to pieces
"""
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import pingouin

stack_overflow = pd.read_feather(".\data\stack_overflow.feather")
# print(stack_overflow.head())

# Job satisfaction: 5 categories
stack_overflow['job_sat'].value_counts()

# Visualizing multiple distributions
# # Is mean annual compensation different for different levels of job satisfaction?
sns.boxplot(x="converted_comp",
            y="job_sat",
            data=stack_overflow)
plt.show()

# Analysis of variance (ANOVA)
alpha = 0.2

pingouin.anova(data=stack_overflow,
               dv="converted_comp",
               between="job_sat")

# pairwise_ttests()
pingouin.pairwise_ttests(data=stack_overflow,
                         dv="converted_comp",
                         between="job_sat",
                         padjust="none")

# Bonferroni correction
pingouin.pairwise_ttests(data=stack_overflow,
                         dv="converted_comp",
                         between="job_sat",
                         padjust="bonf")

# More methods
# # padjust : string
# Method used for testing and adjustment of pvalues.
# # 'none' : no correction [default]
# # 'bonf' : one-step Bonferroni correction
# # 'sidak' : one-step Sidak correction
# # 'holm' : step-down method using Bonferroni adjustments
# # 'fdr_bh' : Benjamini/Hochberg FDR correction
# # 'fdr_by' : Benjamini/Yekutieli FDR correction
