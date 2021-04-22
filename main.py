import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

hugs_data = pd.read_csv('HUG-ds.csv', sep=',')

print(hugs_data)

age_d = hugs_data["age"]
mean = age_d.mean()
sigma = age_d.std()
min = age_d.min()
max = age_d.max()
q1 = float(age_d.quantile([0.25]))
q3 = float(age_d.quantile([0.75]))

age_d_np = age_d.values
print(age_d)
print(age_d_np)
print('>>')
print(mean, sigma, min, max, q1, q3)
print('<<')
plt.boxplot(age_d_np, labels=['Age Distribution (All)'], meanline=True, showmeans=True)
plt.show()
