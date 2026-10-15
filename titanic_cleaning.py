import pandas as pd

# 1. Load Titanic CSV file
df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')

# 2. Handle missing values in 'Age' column using median
df['Age'] = df['Age'].fillna(df['Age'].median())

# 3. Encode 'Sex' column (male -> 0, female -> 1)
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})

# 4. Drop irrelevant columns
df = df.drop(columns=['Cabin', 'Ticket', 'Name'], errors='ignore')

# 5. Save the cleaned dataset to a new CSV file
df.to_csv('titanic_cleaned.csv', index=False)

print("Data cleaning completed successfully!")