import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)
n_samples = 70000

df = pd.DataFrame({
    'id': range(n_samples),
    'age': np.random.randint(10000, 23000, n_samples),
    'gender': np.random.choice([1, 2], n_samples),
    'height': np.random.randint(150, 200, n_samples),
    'weight': np.random.normal(70, 15, n_samples),
    'ap_hi': np.random.randint(90, 200, n_samples),
    'ap_lo': np.random.randint(60, 120, n_samples),
    'cholesterol': np.random.choice([1, 2, 3], n_samples),
    'gluc': np.random.choice([1, 2, 3], n_samples),
    'smoke': np.random.choice([0, 1], n_samples),
    'alco': np.random.choice([0, 1], n_samples),
    'active': np.random.choice([0, 1], n_samples),
    'cardio': np.random.choice([0, 1], n_samples)
})

df['overweight'] = (df['weight'] / ((df['height'] / 100) ** 2) > 25).astype(int)

df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

def draw_cat_plot():
    df_cat = pd.melt(df, 
                     id_vars=['cardio'], 
                     value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')

    fig = sns.catplot(
        data=df_cat,
        x='variable',
        y='total',
        hue='value',
        col='cardio',
        kind='bar'
    ).fig

    fig.savefig('catplot.png')
    return fig

def draw_heat_map():
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    corr = df_heat.corr()

    mask = np.triu(np.ones_like(corr, dtype=bool))

    fig, ax = plt.subplots(figsize=(12, 9))

    sns.heatmap(corr,
                mask=mask,
                annot=True,
                fmt='.1f',
                center=0,
                square=True,
                linewidths=0.5,
                cbar_kws={'shrink': 0.5},
                ax=ax)

    fig.savefig('heatmap.png')
    return fig
