import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
file_path = 'salary.csv'
df = pd.read_csv(file_path)

# Display the first few rows of the DataFrame to understand the structure
print(df.head())

# Clean the salary column by removing the dollar sign and converting it to float
df['Employee Annual Salary'] = df['Employee Annual Salary'].replace('[\$,]', '', regex=True).astype(float)

# Calculate the average salary by department
avg_salary_by_dept = df.groupby('Department')['Employee Annual Salary'].mean().sort_values()

# Display the average salaries
print(avg_salary_by_dept.head())

# Create the bar chart
plt.figure(figsize=(10, 8))
avg_salary_by_dept.plot(kind='barh', color='skyblue')

# Title and labels
plt.title('Average Annual Salary by Department')
plt.xlabel('Average Salary (USD)')
plt.ylabel('Department')

# Display the chart
plt.tight_layout()
plt.show()
