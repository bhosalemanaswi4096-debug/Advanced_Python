
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import zscore

# Sample dataset
data = {
    'Age': [24, 27, 22, 32, 29, 25, 100],
    'Salary': [50000, 60000, 52000, 58000, 62000, 55000, 600000]
}
df = pd.DataFrame(data)

# Descriptive statistics
print("Descriptive Statistics:")
print(df.describe())
print("Mean Age:", df['Age'].mean())
print("Median Age:", df['Age'].median())

# Visualization
plt.hist(df['Age'], bins=5, edgecolor='black')
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

sns.boxplot(y=df['Age'])
plt.title("Box Plot of Age")
plt.show()

plt.scatter(df['Age'], df['Salary'])
plt.title("Age vs Salary")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.show()

sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.show()

# Handling missing data
missing_df = pd.DataFrame({
    'Age': [24, 27, None, 32],
    'Salary': [50000, 60000, 52000, None]
})

print("\nMissing Values:")
print(missing_df.isnull())

print("\nData after filling missing values:")
print(missing_df.fillna(missing_df.mean(numeric_only=True)))

# Detecting and removing outliers
df['Age_zscore'] = zscore(df['Age'])
df['Salary_zscore'] = zscore(df['Salary'])

df_clean = df[
    (df['Age_zscore'].abs() <= 3) &
    (df['Salary_zscore'].abs() <= 3)
]

print("\nData after outlier removal:")
print(df_clean)
