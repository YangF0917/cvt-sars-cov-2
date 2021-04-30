import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

hugs_data = pd.read_csv('HUG-ds.csv', sep=',')

# HUGS All Age Viz.
fig, ax = plt.subplots()
plt.title('Age Distribution of HUGS Data')
age_d = hugs_data["age"]
mean = age_d.mean()
sigma = age_d.std()
min = age_d.min()
max = age_d.max()
q1 = float(age_d.quantile([0.25]))
q3 = float(age_d.quantile([0.75]))

legstr1 = '\n'.join((
    r'$\mu=%.2f$' % (mean,),
    r'$\mathrm{median}=%.2f$' % (age_d.median(),),
    r'$\sigma=%.2f$' % (sigma,),
    r'Q1=%.1f' % (q1,),
    r'Q3=%.1f' % (q3,),
    r'min=%.1f' % (min,),
    r'max=%.1f' % (max,)
    )
)

age_d_np = age_d.values
ax.boxplot(age_d_np, labels=['Age Distribution (All)'], meanline=True, showmeans=True)

props = dict(boxstyle='round', facecolor='white', alpha=0.5)

ax.text(0.05, 0.95, legstr1, transform=ax.transAxes, fontsize=11,
        verticalalignment='top', bbox=props)

# SOURCE DATA- Analysis of SARS-CoV-2 antibodies in COVID-19 convalescent blood using a coronavirus antigen microarray
da2f1a = pd.read_csv('dataA2F1A.csv', sep=',')
for colNum in range(1,len(da2f1a.columns)):
    viz1 = da2f1a.iloc[:, [0, colNum]]
    fig, ax = plt.subplots(figsize=(20, 30))
    plt.gcf().subplots_adjust(bottom=0.3)
    ax.bar(viz1.iloc[:, 0], viz1.iloc[:, 1], width=0.5)
    plt.xticks(rotation='vertical')

# Warning, it generates a lot of graphs, change the indexing above for a particular range
# plt.show()
